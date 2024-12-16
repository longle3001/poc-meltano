"""Stream type classes for tap-google-monitoring."""

from __future__ import annotations

import typing as t
from importlib import resources

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_google_monitoring.client import MySourceNameStream


class InvocationMetricStream(MySourceNameStream):
    """Define custom stream."""

    name = "invocation_metric"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "time"
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"  # noqa: ERA001


    schema = th.PropertiesList(
        th.Property("resource__labels", th.StringType),
        th.Property(
            "resource__type",
            th.StringType,
            description="The user's system ID",
        ),
        th.Property(
            "metric__labels",
            th.StringType,
            description="The user's age in years",
        ),
        th.Property(
            "metric_type",
            th.StringType,
            description="The user's email address",
        ),
        th.Property("point", th.StringType),
        th.Property("time", th.StringType),
        th.Property("id", th.StringType),
        # th.Property("raw_data", th.StringType),

    ).to_dict()



