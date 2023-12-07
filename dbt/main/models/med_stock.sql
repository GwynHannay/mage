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
        qty * size as remaining,
        expiration,
        dose
    from latest_snapshot
    where rownum = 1
        and opened = 'N'
        and qty > 0
), opened as (
    select
        item,
        qty as remaining,
        expiration,
        dose
    from latest_snapshot
    where rownum = 1
        and opened = 'Y'
), current_medications as (
    select * from unopened
    union
    select * from opened
), remaining_medications as (
    select
        item,
        sum(remaining) as remaining,
        min(expiration) as expiration,
        max(dose) as dose,
        now() as today
    from current_medications
    group by item
), calcs as (
    select
        item,
        remaining / dose as days_left,
        {{ next_saturday_from_timestamp('today') }} as next_sorted
    from remaining_medications
)

select
    item,
    remaining,
    expiration,
    dose,
    days_left,
    next_sorted,
	case when days_left < 7 then TRUE else FALSE end as more_needed,
    next_sorted + (days_left::text || ' day')::interval as runs_out
from remaining_medications
join calcs using(item)