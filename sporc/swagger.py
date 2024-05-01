from .sporc_types import Endpoint

# import yaml


def get_yaml_anchors(stream):
    anchors = {}
    loader = yaml.Loader(stream)
    while loader.check_event():
        event = loader.get_event()
        if (
            isinstance(event, yaml.MappingStartEvent)
            or isinstance(event, yaml.ScalarEvent)
        ) and event.anchor is not None:
            raise Exception("Anchors of this type are not yet implemented!")
        if isinstance(event, yaml.SequenceStartEvent) and event.anchor is not None:
            # print(event)
            anchor_name = event.anchor

            event.anchor = None
            events = [event]
            depth = 1

            while depth > 0:
                event = loader.get_event()
                events.append(event)
                if isinstance(event, yaml.SequenceEndEvent):
                    depth -= 1
                elif isinstance(event, yaml.SequenceStartEvent):
                    depth += 1

            anchors[anchor_name] = events

    return anchors


def get_yaml_with_anchors(stream, anchors):
    loader = yaml.Loader(stream)
    events = []
    while loader.check_event():
        event = loader.get_event()
        if isinstance(event, yaml.AliasEvent):
            # print(event)
            if event.anchor not in anchors:
                raise Exception("alias not found!")
            events = events + anchors[event.anchor]
        else:
            events.append(event)

    return yaml.emit(events)


def load_swagger_spec(path: str):
    """Load a swagger yaml spec by path"""

    with open(path) as stream:
        anchors = get_yaml_anchors(stream)

    with open(path) as stream:
        new_stream = get_yaml_with_anchors(stream, anchors)

    return yaml.Loader(new_stream).get_data()


def get_swagger_endpoints(path: str):
    """Return endpoints from the specified swagger spec"""
    endpoints: list[Endpoint] = []
    swagger_spec = load_swagger_spec(path)
    for path, methods in swagger_spec["paths"].items():
        for method, endpoint in methods.items():
            pathParameters = []
            queryParameters = []
            if "parameters" in endpoint:
                for parameter_spec in endpoint["parameters"]:
                    if parameter_spec["in"] == "path":
                        pathParameters.append(parameter_spec["name"])
                    elif parameter_spec["in"] == "query":
                        queryParameters.append(parameter_spec["name"])
            endpoints.append(
                {
                    "name": endpoint["operationId"],
                    "summary": endpoint["summary"] if "summary" in endpoint else "",
                    "method": method.upper(),
                    "path": path,
                    "pathParameters": pathParameters,
                    "queryParameters": queryParameters,
                }
            )
    return endpoints
