## creating a mermaid diagram based on the api_docs.json file
## the api_docs.json file contains some tags, which will be the nodes of the diagram
## in the 'paths', there are some enum parameters which show the attributes of those nodes
## sometimes the api needs some input id in order to retrieve the data.

import json

mermaid_text = "classDiagram \n"

# load the api_docs.json file
api_docs = json.load(open('api_docs.json'))
print(api_docs.keys())
# print(api_docs["definitions"]["Studies"].keys())
# get the tags, these will be the classes
tags = [tag["name"] for tag in api_docs['tags']]

# print(mermaid_text)
tag_to_definition = {}
for path, info in api_docs["paths"].items():
  
  if "get" in info:
    response = info["get"]["responses"]["200"]["schema"]
    if "items" in response:
      if "$ref" in response["items"]:
        # print(path)
        tag_to_definition[info["get"]["tags"][0]] = response["items"]["$ref"].split("/")[-1]

        # print(info["get"]["tags"])

        # print(response["items"]["$ref"])
        # print()

# print(set(tags) - set(tag_to_definition.keys()))
# print(tags)
tag_to_object = {}
for definition, data in api_docs["definitions"].items():
    if definition not in tag_to_definition.values():
       continue
    
    # print(definition)
    if "required" not in data:
      continue
    tag_to_object[definition] = data["required"][0]
    # print(data["required"][1:-1])
    mermaid_text += f"class {definition}{{ \n"
    for attribute, value in data['properties'].items():
      if "type" in value:
        # print(attribute)
        if attribute not in data["required"][1:]:
          mermaid_text += f"    +{value['type']}: {attribute} \n"
    
    mermaid_text += f" }}\n"

relations = ""
for definition, data in api_docs["definitions"].items():
    if definition not in tag_to_definition.values():
       continue
    print(definition)
    for attribute, value in data['properties'].items():
      print("\t", attribute, value)
      obj = None
     
      # optional
      for obj, identifier in tag_to_object.items():
        if attribute == identifier:
          if definition != obj:
            s = f" {definition} --> {obj} \n"
            print(s)
            relations += s
            
      if "$ref" in value:
        val = value['$ref'].split('/')[-1]
        if obj == val:
          continue
        s: str =  f" {definition} --> {val} \n"
        relations +=s
      if "type" in value:
        if value["type"] == "array":
          if "$ref" in value["items"]:
            relations += f" {definition} --> {value['items']['$ref'].split('/')[-1]} \n"



# for subject,identifier in tag_to_object.items():
#   # for prop in valueProps:
#   if identifier.endswith("Id"):
#     print(subject, identifier)
#   for obj, objProps in tag_to_object.items():
#     if subject == obj:
#       continue
    # if valueProps[0] in objProps:
    #   mermaid_text += f"{obj} --|> {subject}\n"
      # print(obj, subject)

# print("\n".join(set(relations.split("\n"))))
print(mermaid_text+ "\n"+ "\n".join(set(relations.split("\n"))))


