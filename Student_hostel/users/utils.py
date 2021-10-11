def normalize_index_number(index: str) -> str:
    try:
        index_number: str = index.lower()
    except Exception:
        raise ValueError(_('Invalid Index Number'))
    if (index_number.startswith("bs") and len(index_number) == 11):
        return index_number
    else:
        raise ValueError(_('Invalid Index Number'))
