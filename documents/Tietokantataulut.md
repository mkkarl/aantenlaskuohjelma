# Tietokantataulut

Users
- id
- username
- password_hash
- *(henkilötietoja)*
- admin (boolean)

Rights
- id
- rightname

Userrights
- user_id
- right_id
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
- *(jollain tapaa laskentakierroksen tulos)*