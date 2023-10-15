with latest_snapshot as (
    select
        item,
        qty,
        opened,
        size,
        expiration,
        dose,
        days,
        last_date,
        row_number() over(partition by item, opened, size order by _mage_updated_at desc) as rownum
    from {{ source('meds_vitamins', 'stock_detail') }}

)

select
    *
from latest_snapshot
where rownum = 1