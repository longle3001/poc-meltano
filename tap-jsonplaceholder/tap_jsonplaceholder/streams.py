"""Stream type classes for tap-jsonplaceholder."""

from singer_sdk import typing as th # JSON Schema typing helpers

from tap_jsonplaceholder.client import jsonplaceholderStream


class CommentsStream(jsonplaceholderStream):
    primary_keys = ["id"]
    path = '/comments'
    name = "comments"
    schema = th.PropertiesList(
        th.Property("postId", th.IntegerType),
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("email", th.StringType),
        th.Property("body", th.StringType),
    ).to_dict()