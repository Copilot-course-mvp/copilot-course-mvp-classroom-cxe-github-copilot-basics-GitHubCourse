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
    raise NotImplementedError("Implement with Copilot translation assistance")