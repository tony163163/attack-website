module_name = "attack_redirections"
priority = 8.2

# Resources redirection json location
attack_redirections_location = "modules/attack_redirections/attack_redirections.json"

# General redirects
general_redirects_dict = {
    "attack-pattern": {"old": "Technique", "new": "techniques"}, 
    "malware": {"old": "Software", "new": "software"},
    "tool": {"old": "Software", "new": "software"},
    "intrusion-set": {"old": "Group", "new": "groups"}
}

general_redirects_types_dict = [
    ["attack-pattern"], 
    ["malware", "tool"], 
    ["intrusion-set"]
]

# Mobile redirects
mobile_redirect_dict = {
    "course-of-action": {
        "old": "Mitigation", 
        "new": "mitigations"
    }
}

mobile_redirect_types_dict = [
    ["course-of-action"]
]

# File paths dictionary
redirects_paths = {
    'enterprise-attack': "wiki/", 
    'mobile-attack': "mobile/index.php/"
}