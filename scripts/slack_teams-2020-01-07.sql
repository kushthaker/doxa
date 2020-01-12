--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5
-- Dumped by pg_dump version 11.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: slack_teams; Type: TABLE DATA; Schema: public; Owner: pgmaster
--

INSERT INTO public.slack_teams (id, api_scope, slack_team_api_id, slack_team_name, api_access_token, last_updated, authenticated_at) VALUES (1, 'identify,channels:history,groups:history,im:history,mpim:history,channels:read,groups:read,im:read,mpim:read,reactions:read,reminders:read,team:read,users:read,users:read.email,usergroups:read,dnd:read,users.profile:read,reminders:write,dnd:write,links:read', 'TGDAJ0S3E', 'doxa', 'xoxp-557358026116-624877030629-842613823666-af71a50cec9e1f4dfeb6cc89f84f5f18', '2019-12-02 01:06:16.115927', NULL);


--
-- Name: slack_teams_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pgmaster
--

SELECT pg_catalog.setval('public.slack_teams_id_seq', 1, true);


--
-- PostgreSQL database dump complete
--

