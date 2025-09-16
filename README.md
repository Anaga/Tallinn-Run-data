# Tallinn-Run-data
This repo is to have local copy on run results in Tallinn

Some endpoints from a "jooks.ee":
* 10 Km, all data: "https://www.jooks.ee/s/json/eyJhY3Rpb24iOiJzaV9yZXN1bHRzX3Jvd3NfanNvbiIsImxhbmdfaWQiOiIxIiwiY29tcGV0aXRpb25faWQiOiIiLCJkaXN0YW5jZV9pZCI6Ijc4NSIsImdlbmRlcl9pZCI6ImdlbmRlcl9pZCIsInYiOiIyMDI1MDkxNF8wODM5MDFfMjIiLCJuY2lkIjoiNTk4In0=.json"
* 21 Km, all data: "https://www.jooks.ee/s/json/eyJhY3Rpb24iOiJzaV9yZXN1bHRzX3Jvd3NfanNvbiIsImxhbmdfaWQiOiIxIiwiY29tcGV0aXRpb25faWQiOiIiLCJkaXN0YW5jZV9pZCI6Ijc4NCIsImdlbmRlcl9pZCI6ImdlbmRlcl9pZCIsInYiOiIyMDI1MDkxNV8xMTIyNDJfMjIiLCJuY2lkIjoiNTk4In0=.json"
* 42 Km, all data: "https://www.jooks.ee/s/json/eyJhY3Rpb24iOiJzaV9yZXN1bHRzX3Jvd3NfanNvbiIsImxhbmdfaWQiOiIxIiwiY29tcGV0aXRpb25faWQiOiIiLCJkaXN0YW5jZV9pZCI6Ijc4MyIsImdlbmRlcl9pZCI6ImdlbmRlcl9pZCIsInYiOiIyMDI1MDkxNV8xMTIyNDJfMjIiLCJuY2lkIjoiNTk4In0=.json"

How to get it with a curl:

curl "https://www.jooks.ee/s/json/eyJhY3Rpb24iOiJzaV9yZXN1bHRzX3Jvd3NfanNvbiIsImxhbmdfaWQiOiIxIiwiY29tcGV0aXRpb25faWQiOiIiLCJkaXN0YW5jZV9pZCI6Ijc4NSIsImdlbmRlcl9pZCI6ImdlbmRlcl9pZCIsInYiOiIyMDI1MDkxNF8wODM5MDFfMjIiLCJuY2lkIjoiNTk4In0=.json"

curl "https://www.jooks.ee/s/json/eyJhY3Rpb24iOiJzaV9yZXN1bHRzX3Jvd3NfanNvbiIsImxhbmdfaWQiOiIxIiwiY29tcGV0aXRpb25faWQiOiIiLCJkaXN0YW5jZV9pZCI6Ijc4MyIsImdlbmRlcl9pZCI6ImdlbmRlcl9pZCIsInYiOiIyMDI1MDkxNV8xMTIyNDJfMjIiLCJuY2lkIjoiNTk4In0=.json" > 2025_Run\2025.09.13_Run_42_Km.json

script usage:
 python json_to_csv_converter.py -i 2025_Run\2025.09.13_Run_21_Km.json -o 2025_Run\2025.09.13_Run_21_Km.csv
 python json_to_csv_converter.py -i 2025_Run\2025.09.13_Run_42_Km.json -o 2025_Run\2025.09.13_Run_42_Km.csv