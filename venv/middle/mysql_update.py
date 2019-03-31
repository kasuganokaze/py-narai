from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import (
    DeleteRowsEvent,
    UpdateRowsEvent,
    WriteRowsEvent
)
import sys
import json


def main():
    stream = BinLogStreamReader(
        connection_settings={
            "host": '127.0.0.1',
            "port": 3306,
            "user": 'root',
            "passwd": '12345Aa.',
        },
        server_id=1,
        blocking=True,
        resume_stream=True,
        only_events=[DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent],
        auto_position=0,
    )

    for bin_log_event in stream:
        for row in bin_log_event.rows:
            event = {"schema": bin_log_event.schema, "table": bin_log_event.table,
                     "log_pos": bin_log_event.packet.log_pos}
            if isinstance(bin_log_event, DeleteRowsEvent):
                event["action"] = "delete"
                event["values"] = dict(row["values"].items())
                event = dict(event.items())
            elif isinstance(bin_log_event, UpdateRowsEvent):
                event["action"] = "update"
                event["before_values"] = dict(row["before_values"].items())
                event["after_values"] = dict(row["after_values"].items())
                event = dict(event.items())
            elif isinstance(bin_log_event, WriteRowsEvent):
                event["action"] = "insert"
                event["values"] = dict(row["values"].items())
                event = dict(event.items())
            json.dumps(event)
            sys.stdout.flush()

    stream.close()


if __name__ == "__main__":
    main()
