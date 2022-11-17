# Tietokantataulut

Users
- id
- username
- password_hash
- *(henkilötietoja)*
- admin (boolean)

Officers
- user_id
- meeting_id
- meetingofficer (boolean)
- votecounter (boolean)

Meetings
- id
- name
- date
- time

Elections
- id
- meeting_id
- name

Candidates
- id
- election_id
- name

Votes
- id
- election_id
- log

Votes_Candidates
- vote_id
- canditate_id
- placing_number

Counting_rounds
- id
- election_id
- round_nr

Counting_round_Canditate
- Round_id
- canditate_id
