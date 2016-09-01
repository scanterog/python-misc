from flask import Flask, jsonify, make_response, abort, request, url_for, json

app = Flask(__name__)
objects = []


@app.errorhandler(400)
def bad_request(error):
    """ Return 400 error in JSON format. """
    return make_response(jsonify({'error': error.description}), 400)


@app.errorhandler(404)
def not_found(error):
    """ Return 404 error in JSON format. """
    return make_response(jsonify({'error': error.description}), 404)


def validate_params(identifier, ranges):
    """ Validate identifier and ranges attributes from a new object.

    The Identifer attribute must be a string and must not be null.
    The Ranges attribute must be a list of lists. Every list must have only two
    elements.

    Return value is a tuple(bool, string). The bool value is True if all the
    parameters all valid or False is at least one of them is invalid.
    The string value contains the error message when the attribute is invalid
    and is empty when all the parameters are correct.
    """
    if not isinstance(identifier, basestring) or len(identifier) == 0:
        return False, "Object ID not valid"

    try:
        ranges_list = json.loads(ranges)
    except ValueError:
        return False, "Invalid range"

    if type(ranges_list) != list:
        return False, "Invalid range"

    if len(ranges_list) > 0 and all(isinstance(l, list) and
                                    len(l) == 2 for l in ranges_list):
        return True, ""
    else:
        return False, "Invalid format range"


@app.route('/qengine/api/v1.0/objects', methods=['POST'])
def store_object():
    """ Store object sent by POST request.

    If the identifier doesn't exist, a new object is created.
    If the identifier already exist, the object is overwritten.
    Return value is the JSON representation of the new object.
    """
    if not request.json or not'identifier' in request.json or \
            not'ranges' in request.json:
        abort(400)

    valid, error_msg = validate_params(request.json['identifier'],
                                       request.json['ranges'])
    if not valid:
        abort(400, error_msg)

    exist = False
    for o in objects:
        if request.json['identifier'] == o['identifier']:
            exist = True
            o['ranges'] = json.loads(request.json['ranges'])

    if not exist:
        obj = {}
        obj['identifier'] = request.json['identifier']
        obj['ranges'] = json.loads(request.json['ranges'])
        objects.append(obj)

    return json.dumps(objects), 201, {'Content-Type': 'application/json'}


@app.route('/qengine/api/v1.0/objects/<start>/<end>', methods=['GET'])
def retrieve_overlap_objects(start, end):
    """ Retrieve a list of object whose range overlap a specified range.

    The list [a,b] sent by the client is encoded in the following format:
    http://hostname/qengine/api/v1.0/objects/<start>/<end> where <start>
    represent "a" and <end> represent b.
    Return value is the JSON representation of the list of objects whose
    overlap the specified range.
    """
    try:
        s = int(start)
        e = int(end)
    except ValueError:
        abort(400, "Range value must be an integer value")

    if s > e:
        abort(400, "End value should be lower that start value")

    result = []
    for o in objects:
        for l in o.get('ranges'):
                intersection = set(range(l[0], l[1])).intersection(range(s, e))
                if len(intersection) > 0:
                    t = o.copy()
                    t['intersection'] = len(intersection)
                    result.append(t)

    return json.dumps(result), {'Content-Type': 'application/json'}


@app.route('/qengine/api/v1.0/objects', methods=['GET'])
def get_objects():
    """Return value is the JSON representation of all objects."""
    return json.dumps(objects), {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run()
