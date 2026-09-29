--
-- PostgreSQL database dump
--

\restrict 9PssgS1pAVzfIrmgkl9d77tGSqbjjPlGEDD3IOs4o5vpxUVAgEDo8KOzRdSrYws

-- Dumped from database version 16.15
-- Dumped by pg_dump version 16.15

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: inferencias; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.inferencias (
    id integer NOT NULL,
    fecha timestamp without time zone DEFAULT now() NOT NULL,
    motor character varying(20) NOT NULL,
    modelo character varying(120) NOT NULL,
    entrada text NOT NULL,
    salida text NOT NULL,
    latencia_ms integer NOT NULL
);


ALTER TABLE public.inferencias OWNER TO postgres;

--
-- Name: inferencias_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.inferencias_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.inferencias_id_seq OWNER TO postgres;

--
-- Name: inferencias_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.inferencias_id_seq OWNED BY public.inferencias.id;


--
-- Name: inferencias id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.inferencias ALTER COLUMN id SET DEFAULT nextval('public.inferencias_id_seq'::regclass);


--
-- Data for Name: inferencias; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.inferencias (id, fecha, motor, modelo, entrada, salida, latencia_ms) FROM stdin;
1	2026-09-29 02:32:46.470107	eco	reglas-v1	feat: login con token	feat	12
2	2026-09-29 02:32:46.470107	eco	reglas-v1	fix: corregir error de boton	fix	15
\.


--
-- Name: inferencias_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.inferencias_id_seq', 2, true);


--
-- Name: inferencias inferencias_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.inferencias
    ADD CONSTRAINT inferencias_pkey PRIMARY KEY (id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pg_database_owner
--

GRANT USAGE ON SCHEMA public TO app_ia;


--
-- Name: TABLE inferencias; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT ON TABLE public.inferencias TO app_ia;


--
-- Name: SEQUENCE inferencias_id_seq; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,USAGE ON SEQUENCE public.inferencias_id_seq TO app_ia;


--
-- PostgreSQL database dump complete
--

\unrestrict 9PssgS1pAVzfIrmgkl9d77tGSqbjjPlGEDD3IOs4o5vpxUVAgEDo8KOzRdSrYws

