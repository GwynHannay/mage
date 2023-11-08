with latest_snapshot as (
    select
        item,
        cast(qty as int) as qty,
        opened,
        cast(size as int) as size,
        expiration,
        cast(dose as int) as dose,
        days,
        last_date,
        row_number() over(partition by item, opened, size order by _mage_updated_at desc) as rownum
    from {{ source('meds_vitamins', 'stock_detail') }}
), unopened as (
    select
        item,
        qty,
        size,
        expiration,
        dose,
        qty * size as remaining
    from latest_snapshot
    where rownum = 1
        and opened = 'N'
        and qty > 0
), opened as (
    select
        item,
        qty,
        size,
        expiration,
        dose
    from latest_snapshot
    where rownum = 1
        and opened = 'Y'
), next_saturday as (
    select 
        6 - extract(dow from now()) sa days_from_sat
)

select
    *
from unopened