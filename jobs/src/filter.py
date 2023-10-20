ACCEPTABLE_TAGS = ["AI/ML", "ML Engineer", "AI Engineer", "Software Engineer", 
                    "Data Scientist", "Computer Vision", "Data Engineer",
                    "Machine Learning Engineer", "Artificial Intelligence"]

UNACCEPTABLE_TAGS = ["Manager", "Leader", "Staff", "Principal"]

def filter_out_titles(list_jobs):
    # Perform filtration
    print("Filtering...")
    new_jobs = []
    for j in list_jobs:

        title = j['title'].lower()
        # Validate has at least one of the acceptable tags
        good = False
        for a in ACCEPTABLE_TAGS:
            if a.lower() in title:
                good = True
                break
        if not good:
            continue

        # Validate that it has none of the unacceptable tags
        good = True
        for u in UNACCEPTABLE_TAGS:
            if u.lower() in title:
                good = False
                break
        if not good:
            continue

        new_jobs.append(j)

    print(f"Filtered jobs down to list of {len(new_jobs)}")
    return new_jobs
