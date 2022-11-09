# Tietokantataulut

Users
- id
- username
- password_hash
- *(henkilötietoja)*
- admin (boolean)

Officer_type
- id
- officename

User_Officer
- user_id
- office_id
- meeting_id

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
