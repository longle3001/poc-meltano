"""Custom client handling, including MySourceNameStream base class."""

# pip install google-auth google-cloud-monitoring

from __future__ import annotations

import typing as t
from typing import Iterable, List, Optional, Tuple

from singer_sdk.streams import Stream
from singer_sdk.streams.core import REPLICATION_FULL_TABLE, REPLICATION_INCREMENTAL

from google.cloud import monitoring_v3
from datetime import datetime, timedelta
# import pytz
from google.oauth2 import service_account
import json
import uuid



if t.TYPE_CHECKING:
    from singer_sdk.helpers.types import Context


class MySourceNameStream(Stream):
    """Stream class for MySourceName streams."""
    def _get_credential_from_config(
            self
    ):
        return {
            "type": self._config["type"],
            "project_id": self._config["project_id"],
            "private_key_id": self._config["private_key_id"],
            "private_key": self._config["private_key"],
            "client_email": self._config["client_email"],
            "client_id": self._config["client_id"],
            "auth_uri":  self._config["auth_uri"],
            "token_uri":  self._config["token_uri"],
            "auth_provider_x509_cert_url":  self._config["auth_provider_x509_cert_url"],
            "client_x509_cert_url":  self._config["client_x509_cert_url"],
            "universe_domain":  self._config["universe_domain"],
        }
    
    def _get_record(
            self,
            context: Optional[dict],
    ):
        credentials_dict = self._get_credential_from_config()
        credentials = service_account.Credentials.from_service_account_info(credentials_dict)
        client = monitoring_v3.MetricServiceClient(credentials=credentials)

        project_id = self._config["project_id"]
        metric_type = self._config["metric_type"]
        resource_type = self._config["resource_type"]
        end_time = datetime.now()
        start_time = end_time - timedelta(days=14)  # Last 2 weeks
        if self.get_starting_replication_key_value(context):
            starting_replication_time = self.get_starting_replication_key_value(context)
            start_time = datetime.fromisoformat(starting_replication_time)
        interval_minutes = 1


        project_name = f"projects/{project_id}"
        interval = monitoring_v3.TimeInterval(
            {
                "start_time": {"seconds": int(start_time.timestamp())},
                "end_time": {"seconds": int(end_time.timestamp())},
            }
        )
        aggregation = monitoring_v3.Aggregation(
            {
                "alignment_period": {"seconds": interval_minutes * 60},
                "per_series_aligner": monitoring_v3.Aggregation.Aligner.ALIGN_RATE,
            }
        )

        # Adjust the filter to include resource type
        filter_str = (
            # f'metric.type = "{metric_type}" '
            f'metric.type = "{metric_type}" AND '
            f'resource.type = "{resource_type}"'
        )

        # for descriptor in client.list_metric_descriptors(name=project_name):
        #     print(descriptor.type)
                
        results = client.list_time_series(
            request={
                "name": project_name,
                "filter": filter_str,
                "interval": interval,
                "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
                "aggregation": aggregation,
            }
        )
        return results


    def get_records(
        self,
        context: Optional[dict],
    ) -> t.Iterable[dict]:
        """Return a generator of record-type dictionary objects.

        The optional `context` argument is used to identify a specific slice of the
        stream if partitioning is required for the stream. Most implementations do not
        require partitioning and should ignore the `context` argument.

        Args:
            context: Stream partition or context dictionary.

        Raises:
            NotImplementedError: If the implementation is TODO
        """

        results = self._get_record(context)
        for result in results:
            for point in result.points:
                record = {
                    "resource__labels": json.dumps(dict(result.resource.labels)),
                    "resource__type": result.resource.type,
                    "metric__labels": json.dumps(dict(result.metric.labels)),
                    "metric_type": result.metric.type,
                    "point": str(point.value.double_value),
                    "time": str(point.interval.end_time),
                    "id": str(uuid.uuid4()),
                    # "id":  self._get_state_partition_context(context)
                    # "id": self.replication_method 
                    # "id": self.child_streams
                    # "id": self.replication_key
                    # "id": state
                    # "resource__labels": a,
                    # "resource__type": state,
                    # "metric__labels": self.get_starting_replication_key_value(context),
                    # "metric_type": start_time,

                }
                yield record
