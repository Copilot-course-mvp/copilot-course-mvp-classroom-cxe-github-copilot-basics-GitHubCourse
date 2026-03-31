# JavaScript reference implementation:
#
# function groupByDomain(emails) {
#   const counts = {};
#   for (const email of emails) {
#     if (!email.includes('@')) continue;
#     const domain = email.split('@')[1].trim().toLowerCase();
#     if (!domain) continue;
#     counts[domain] = (counts[domain] || 0) + 1;
#   }
#   return Object.fromEntries(Object.entries(counts).sort(([a], [b]) => a.localeCompare(b)));
# }


def group_by_domain(emails: list[str]) -> dict[str, int]:
    """Translate the JavaScript behavior above into Python."""
    counts: dict[str, int] = {}
    for email in emails:
        if "@" not in email:
            continue
        domain = email.split("@")[1].strip().lower()
        if not domain:
            continue
        counts[domain] = counts.get(domain, 0) + 1
    return dict(sorted(counts.items()))