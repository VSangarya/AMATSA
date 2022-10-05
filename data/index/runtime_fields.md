# Runtime fields

In Elasticsearch Stack Management, goto Data Views under Kibana, open the dataview for your index and setup the following runtime fields:

1. metrics.used_memory_gb
type: double
value: emit(doc['agent.total_memory_gb'].value - doc['metrics.avail_memory_gb'].value)
