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
-- Data for Name: slack_conversations; Type: TABLE DATA; Schema: public; Owner: pgmaster
--

INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (23, 'GQWDGLFV2', 1, 'mpim', 'mpdm-lauriermantel--kushthaker--mitccall-1', false, '2020-01-07 20:00:02.760635');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (48, 'DQ766DU3S', 1, 'im', NULL, false, '2020-01-07 20:00:02.769823');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (20, 'GQ1EAN6NT', 1, 'private_channel', 'zzz11', false, '2020-01-07 20:00:01.04157');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (22, 'GQRPL9A2X', 1, 'private_channel', 'test-private', false, '2020-01-07 20:00:01.066484');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (41, 'GR3CADR0D', 1, 'private_channel', 'test-priv2', true, '2020-01-07 20:00:01.083063');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (24, 'DQ766DUTA', 1, 'im', NULL, false, '2020-01-07 20:00:01.092614');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (25, 'DPYQGDJ2J', 1, 'im', NULL, false, '2020-01-07 20:00:01.1065');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (27, 'DPAEA4DV1', 1, 'im', NULL, false, '2020-01-07 20:00:01.125162');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (29, 'DGEU344H4', 1, 'im', NULL, false, '2020-01-07 20:00:01.143604');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (30, 'DGEE56GLX', 1, 'im', NULL, false, '2020-01-07 20:00:01.152832');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (31, 'DGDATJN84', 1, 'im', NULL, false, '2020-01-07 20:00:01.161913');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (33, 'DQ766DT08', 1, 'im', NULL, false, '2020-01-07 20:00:01.537986');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (35, 'DPHQP46D8', 1, 'im', NULL, false, '2020-01-07 20:00:01.557441');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (36, 'DP953Q3EE', 1, 'im', NULL, false, '2020-01-07 20:00:01.569078');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (38, 'DGEU343PG', 1, 'im', NULL, false, '2020-01-07 20:00:01.584592');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (39, 'DGEDVJFST', 1, 'im', NULL, false, '2020-01-07 20:00:01.59532');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (40, 'DGEDVJFFH', 1, 'im', NULL, false, '2020-01-07 20:00:01.607595');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (32, 'DGD8HTE4T', 1, 'im', NULL, false, '2020-01-07 20:00:01.635954');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (21, 'GQQEF4ZAN', 1, 'mpim', 'mpdm-lauriermantel--fulfilled_ai--lwdmante-1', false, '2020-01-07 20:00:02.197483');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (42, 'DQ91Z0UMD', 1, 'im', NULL, false, '2020-01-07 20:00:02.223951');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (26, 'DPXBVSBN2', 1, 'im', NULL, false, '2020-01-07 20:00:02.245772');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (43, 'DPWJAK81E', 1, 'im', NULL, false, '2020-01-07 20:00:02.255619');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (34, 'DPV5YJDJ9', 1, 'im', NULL, false, '2020-01-07 20:00:02.26656');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (45, 'DPUMG37L4', 1, 'im', NULL, false, '2020-01-07 20:00:02.305959');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (46, 'DPM8GFZGR', 1, 'im', NULL, false, '2020-01-07 20:00:02.316615');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (47, 'DPM8GFXDX', 1, 'im', NULL, false, '2020-01-07 20:00:02.323897');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (12, 'CPEHV1VGS', 1, 'public_channel', 'prototyping', true, '2020-01-07 20:00:02.676948');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (13, 'CPLN78H6W', 1, 'public_channel', 'zzz5', false, '2020-01-07 20:00:02.687861');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (14, 'CPN201D19', 1, 'public_channel', 'zzz1', false, '2020-01-07 20:00:02.697716');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (15, 'CPZFX2Z9N', 1, 'public_channel', 'zzz6', false, '2020-01-07 20:00:02.710486');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (16, 'CPZFX8AC8', 1, 'public_channel', 'zzz7', false, '2020-01-07 20:00:02.717029');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (17, 'CPZG34T6H', 1, 'public_channel', 'zzz2', false, '2020-01-07 20:00:02.726694');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (18, 'CQ1BN6U79', 1, 'public_channel', 'zzz4', false, '2020-01-07 20:00:02.735118');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (19, 'CQ1N0TWUE', 1, 'public_channel', 'zzz3', false, '2020-01-07 20:00:02.75453');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (1, 'CGD8ER3HR', 1, 'public_channel', 'eng', false, '2020-01-07 20:00:02.531104');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (2, 'CGDAJ1K1A', 1, 'public_channel', 'product', false, '2020-01-07 20:00:02.537616');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (3, 'CGDDN7RS6', 1, 'public_channel', 'frameworks', false, '2020-01-07 20:00:02.560268');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (4, 'CGDPL3CJZ', 1, 'public_channel', 'other-ideas', false, '2020-01-07 20:00:02.580806');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (5, 'CGEDVJHPH', 1, 'public_channel', 'general', false, '2020-01-07 20:00:02.594179');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (6, 'CGEDVJKPZ', 1, 'public_channel', 'random', false, '2020-01-07 20:00:02.611788');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (7, 'CK5V37NCS', 1, 'public_channel', 'advice-mentorship', false, '2020-01-07 20:00:02.623857');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (8, 'CLM8KB11T', 1, 'public_channel', 'meeting-planning', false, '2020-01-07 20:00:02.641049');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (9, 'CLMNJJN6M', 1, 'public_channel', 'design', false, '2020-01-07 20:00:02.646214');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (10, 'CMUKLK4HL', 1, 'public_channel', 'bet-300', false, '2020-01-07 20:00:02.654292');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (11, 'CPDANB4UV', 1, 'public_channel', 'syde-461', false, '2020-01-07 20:00:02.66132');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (49, 'DPYQGDL86', 1, 'im', NULL, false, '2020-01-07 20:00:02.77933');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (44, 'DPUMG3952', 1, 'im', NULL, false, '2020-01-07 20:00:02.781954');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (50, 'DP953Q550', 1, 'im', NULL, false, '2020-01-07 20:00:02.790276');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (28, 'DJEMXU76K', 1, 'im', NULL, false, '2020-01-07 20:00:02.798671');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (51, 'DJEMXU37H', 1, 'im', NULL, false, '2020-01-07 20:00:02.806889');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (37, 'DJCT71VFA', 1, 'im', NULL, false, '2020-01-07 20:00:02.81844');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (52, 'DJ6H427SM', 1, 'im', NULL, false, '2020-01-07 20:00:02.831047');
INSERT INTO public.slack_conversations (id, slack_conversation_api_id, slack_team_id, conversation_type, conversation_name, is_deleted, last_updated) VALUES (53, 'DJ6H42001', 1, 'im', NULL, false, '2020-01-07 20:00:02.836026');


--
-- Name: slack_conversations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pgmaster
--

SELECT pg_catalog.setval('public.slack_conversations_id_seq', 53, true);


--
-- PostgreSQL database dump complete
--

