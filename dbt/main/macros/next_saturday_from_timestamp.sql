{%  macro next_saturday_from_timestamp(timestamp_with_tz) %}
    date_trunc('day', timestamp_with_tz + ((6 - extract(dow from timestamp_with_tz))::text || ' day')::interval)
{% endmacro %}