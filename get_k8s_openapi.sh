#!/bin/bash

cluster_id=${1:-apps-yellow.dev.zg-itx.net}

kubectx "${cluster_id}"

kubectl create serviceaccount api-explorer

kubectl create rolebinding api-explorer:cluster-admin --clusterrole cluster-admin --serviceaccount default:api-explorer

# Get the ServiceAccount's token Secret's name
SECRET=$(kubectl get serviceaccount api-explorer -o json | jq -Mr '.secrets[].name | select(contains("token"))')
# Extract the Bearer token from the Secret and decode
TOKEN=$(kubectl get secret ${SECRET} -o json | jq -Mr '.data.token' | base64 -D)
# Extract, decode and write the ca.crt to a temporary location
kubectl get secret ${SECRET} -o json | jq -Mr '.data["ca.crt"]' | base64 -D > /tmp/ca.crt
# Get the API Server location
# IFS=, APISERVERS=($(kubectl -n default get endpoints kubernetes --no-headers | awk '{ print $2 }'))
APISERVER=$(cat ~/.kube/config| yq --arg cluster_id "${cluster_id}" '.clusters[] | select(.name==$cluster_id) | .cluster.server' -r)
curl -s "${APISERVER}/openapi/v2"  --header "Authorization: Bearer $TOKEN" --cacert /tmp/ca.crt | json_pp
