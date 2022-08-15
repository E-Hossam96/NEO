"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    neos = []
    with open(neo_csv_path, 'r') as fid_csv:
        reader = csv.reader(fid_csv)
        next(reader)
        for line in reader:
            try:
                obj = [line[3], line[7], line[4], float(line[15])]
            except ValueError:
                obj = [line[3], line[7], line[4], float('nan')]
            obj[1] = True if obj[1] == 'Y' else False
            neos.append(obj)
    
    # indices of needed data are:
    # 3: pdes, 4: name, 7: pha, 15: diameter
    return [NearEarthObject(*obj) for obj in neos]


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    with open(cad_json_path, 'r') as fid_json:
        cad = json.load(fid_json)
    
    cad = cad['data']

    # indices of needed data are:
    # 0: pdes, 3: cd, 4: dist, 7: v_rel
    cad = [[obj[0], obj[3], float(obj[4]), float(obj[7])] for obj in cad]
    
    return [CloseApproach(*obj) for obj in cad]
