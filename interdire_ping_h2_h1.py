import requests
data = {"src-ip":"10.0.0.2/32","dst-ip":"10.0.0.1/32","action":"deny","nw-proto":"icmp"}
url = "http://localhost:8080/wm/acl/rules/json"
res = requests.post(url,json= data)
print(res.content)

# pour supprimer la règle :
# curl http://localhost:8080/wm/acl/rules/json | python -mjson.tool
# curl -X DELETE -d '{"ruleid":"1" }' http://localhost:8080/wm/acl/rules/json