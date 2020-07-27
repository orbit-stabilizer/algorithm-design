#!/usr/bin/python3

def stable_matching(men_preferences, women_preferences):
    matching = {} # {woman: man}
    free_men = set(range(len(men_preferences)))
    proposed = {man: set() for man in free_men}

    def successful_proposal(man, woman):
        if not woman in matching: return True
        for preference, man_ in sorted(women_preferences[woman].items(), reverse=True):
            if man_ == man: return True
            if man_ == matching[woman]: return False

    while free_men:
        man = free_men.pop()
        for preference, woman in sorted(men_preferences[man].items(), reverse=True):
            if not woman in proposed[man]:
                proposed[man].add(woman)
                if successful_proposal(man, woman):
                    if woman in matching:
                        free_men.add(matching[woman])
                    matching[woman] = man
                    break

    return matching

if __name__ == '__main__':
    from stable_matching_data import men_preferences, women_preferences

    print(stable_matching(men_preferences, women_preferences))
