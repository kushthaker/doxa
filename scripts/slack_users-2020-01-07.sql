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
-- Data for Name: slack_users; Type: TABLE DATA; Schema: public; Owner: pgmaster
--

INSERT INTO public.slack_users (id, slack_user_api_id, slack_team_id, slack_email_address, first_name, last_name, slack_username, is_authenticated, is_deleted_on_slack, created_date, last_updated, slack_timezone_label, slack_timezone_offset, authentication_oauth_access_token) VALUES (1, 'UGCKJ22GY', 1, 'lauriermantel@gmail.com', 'Laurier', 'Mantel', 'lauriermantel', true, false, '2019-10-29 02:29:22.988556', '2019-11-24 20:15:31.150237', 'Eastern Daylight Time', -14400, 'xoxp-557358026116-556664070576-809038529654-217b7fa9b976205936c17a099f120017');
INSERT INTO public.slack_users (id, slack_user_api_id, slack_team_id, slack_email_address, first_name, last_name, slack_username, is_authenticated, is_deleted_on_slack, created_date, last_updated, slack_timezone_label, slack_timezone_offset, authentication_oauth_access_token) VALUES (3, 'UGDBV8GDQ', 1, 'kushthaker@gmail.com', 'Kush', '', 'kushthaker', true, false, '2019-11-24 20:35:40.548953', '2019-11-24 20:35:40.548955', 'Eastern Standard Time', -18000, 'xoxp-557358026116-557403288466-800155360179-1ef3af27e1dc315f9443b50e91192c61');
INSERT INTO public.slack_users (id, slack_user_api_id, slack_team_id, slack_email_address, first_name, last_name, slack_username, is_authenticated, is_deleted_on_slack, created_date, last_updated, slack_timezone_label, slack_timezone_offset, authentication_oauth_access_token) VALUES (4, 'UPHM989GB', 1, 'lwdmante@edu.uwaterloo.ca', 'testlaurier2mantel', '', 'lwdmante', true, false, '2019-11-29 05:29:48.267078', '2019-11-29 05:29:48.267081', 'Eastern Standard Time', -18000, 'xoxp-557358026116-799723281555-853511273285-db1ac2de0f620d67b0afd25688892d56');
INSERT INTO public.slack_users (id, slack_user_api_id, slack_team_id, slack_email_address, first_name, last_name, slack_username, is_authenticated, is_deleted_on_slack, created_date, last_updated, slack_timezone_label, slack_timezone_offset, authentication_oauth_access_token) VALUES (6, 'UJCRT0WJH', 1, 'mitccall@gmail.com', NULL, NULL, 'mitccall', true, false, '2019-12-02 01:06:16.260949', '2019-12-02 01:06:16.260953', 'Eastern Standard Time', -18000, 'xoxp-557358026116-624877030629-842613823666-af71a50cec9e1f4dfeb6cc89f84f5f18');


--
-- Name: slack_users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pgmaster
--

SELECT pg_catalog.setval('public.slack_users_id_seq', 6, true);


--
-- PostgreSQL database dump complete
--

