"""MySourceName tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_google_monitoring import streams


class TapMySourceName(Tap):
    """MySourceName tap class."""

    name = "tap-google-monitoring"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "type",
            th.StringType,
            required=True,
            title="type",
            description="type",
        ),
        th.Property(
            "project_id",
            th.StringType,
            required=True,
            title="Project ID",
            description="Project ID to replicate",
        ),
        th.Property(
            "private_key_id",
            th.StringType,
            required=True,
            description="private_key_id",
        ),
        th.Property(
            "private_key",
            th.StringType,
            title="private_key",
            required=True,
            # default="https://api.mysample.com",
            description="private_key",
        ),
        th.Property(
            "client_email",
            th.StringType,
            title="client_email",
            required=True,
            description="client_email",
        ),
        th.Property(
            "client_id",
            th.StringType,
            title="client_id",
            required=True,
            description="client_id",
        ),
        th.Property(
            "auth_uri",
            th.StringType,
            title="auth_uri",
            required=True,
            default="https://accounts.google.com/o/oauth2/auth",
            description="auth_uri",
        ),
        th.Property(
            "token_uri",
            th.StringType,
            title="token_uri",
            required=True,
            default="https://oauth2.googleapis.com/token",
            description="token_uri",
        ),

        th.Property(
            "auth_provider_x509_cert_url",
            th.StringType,
            title="auth_provider_x509_cert_url",
            required=True,
            default="https://www.googleapis.com/oauth2/v1/certs",
            description="auth_provider_x509_cert_url",
        ),
        th.Property(
            "client_x509_cert_url",
            th.StringType,
            title="client_x509_cert_url",
            required=True,
            default="https://www.googleapis.com/robot/v1/metadata/x509/lumin-data-sa%40lumin-production-services.iam.gserviceaccount.com",
            description="client_x509_cert_url",
        ),
        th.Property(
            "universe_domain",
            th.StringType,
            title="universe_domain",
            required=True,
            default="googleapis.com",
            description="universe_domain",
        ),
        th.Property(
            "metric_type",
            th.StringType,
            title="metric_type",
            required=True,
            description="metric_type",
        ),
        th.Property(
            "resource_type",
            th.StringType,
            title="resource_type",
            required=True,
            description="resource_type",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.MySourceNameStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.InvocationMetricStream(self),
        ]


if __name__ == "__main__":
    TapMySourceName.cli()
