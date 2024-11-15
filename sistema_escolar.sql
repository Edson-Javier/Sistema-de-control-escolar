PGDMP  ,    *            
    |            sistema_escolar    16.2    16.2 F    :           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ;           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            <           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            =           1262    26260    sistema_escolar    DATABASE     �   CREATE DATABASE sistema_escolar WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE sistema_escolar;
                postgres    false            �            1259    26361    alumno    TABLE     �   CREATE TABLE public.alumno (
    id integer NOT NULL,
    id_grupo integer,
    id_carrera integer,
    nombre character varying(80),
    direccion character varying(80),
    estatus character varying(10),
    semestre integer,
    telefono integer
);
    DROP TABLE public.alumno;
       public         heap    postgres    false            �            1259    26360    alumno_id_alumno_seq    SEQUENCE     �   CREATE SEQUENCE public.alumno_id_alumno_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.alumno_id_alumno_seq;
       public          postgres    false    231            >           0    0    alumno_id_alumno_seq    SEQUENCE OWNED BY     F   ALTER SEQUENCE public.alumno_id_alumno_seq OWNED BY public.alumno.id;
          public          postgres    false    230            �            1259    26262    carrera    TABLE     c   CREATE TABLE public.carrera (
    id integer NOT NULL,
    nombre_carrera character varying(40)
);
    DROP TABLE public.carrera;
       public         heap    postgres    false            �            1259    26261    carrera_id_carrera_seq    SEQUENCE     �   CREATE SEQUENCE public.carrera_id_carrera_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.carrera_id_carrera_seq;
       public          postgres    false    216            ?           0    0    carrera_id_carrera_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.carrera_id_carrera_seq OWNED BY public.carrera.id;
          public          postgres    false    215            �            1259    26308    coordinador    TABLE     _   CREATE TABLE public.coordinador (
    id integer NOT NULL,
    nombre character varying(80)
);
    DROP TABLE public.coordinador;
       public         heap    postgres    false            �            1259    26307    coordinador_id_coordinador_seq    SEQUENCE     �   CREATE SEQUENCE public.coordinador_id_coordinador_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.coordinador_id_coordinador_seq;
       public          postgres    false    225            @           0    0    coordinador_id_coordinador_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.coordinador_id_coordinador_seq OWNED BY public.coordinador.id;
          public          postgres    false    224            �            1259    26321    grupo    TABLE     }   CREATE TABLE public.grupo (
    id_materia integer,
    id_maestro integer,
    id_salon integer,
    id integer NOT NULL
);
    DROP TABLE public.grupo;
       public         heap    postgres    false            �            1259    26353    grupo_id_grupo_seq    SEQUENCE     �   CREATE SEQUENCE public.grupo_id_grupo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.grupo_id_grupo_seq;
       public          postgres    false    228            A           0    0    grupo_id_grupo_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.grupo_id_grupo_seq OWNED BY public.grupo.id;
          public          postgres    false    229            �            1259    26281    maestro    TABLE     �   CREATE TABLE public.maestro (
    id integer NOT NULL,
    nombre character varying(80),
    direccion character varying(80),
    telefono integer,
    especialidad character varying(120)
);
    DROP TABLE public.maestro;
       public         heap    postgres    false            �            1259    26280    maestro_id_maestro_seq    SEQUENCE     �   CREATE SEQUENCE public.maestro_id_maestro_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.maestro_id_maestro_seq;
       public          postgres    false    220            B           0    0    maestro_id_maestro_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.maestro_id_maestro_seq OWNED BY public.maestro.id;
          public          postgres    false    219            �            1259    26287    maestro_materia    TABLE     �   CREATE TABLE public.maestro_materia (
    id_materia integer,
    id_maestro integer,
    horario_clases time without time zone
);
 #   DROP TABLE public.maestro_materia;
       public         heap    postgres    false            �            1259    26269    materia    TABLE     �   CREATE TABLE public.materia (
    id integer NOT NULL,
    id_carrera integer,
    creditos integer,
    nombre_materia character varying(80),
    cupo integer
);
    DROP TABLE public.materia;
       public         heap    postgres    false            �            1259    26268    materia_id_materia_seq    SEQUENCE     �   CREATE SEQUENCE public.materia_id_materia_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.materia_id_materia_seq;
       public          postgres    false    218            C           0    0    materia_id_materia_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.materia_id_materia_seq OWNED BY public.materia.id;
          public          postgres    false    217            �            1259    26315    salon    TABLE     p   CREATE TABLE public.salon (
    id integer NOT NULL,
    nombre character varying(10),
    capacidad integer
);
    DROP TABLE public.salon;
       public         heap    postgres    false            �            1259    26314    salon_id_salon_seq    SEQUENCE     �   CREATE SEQUENCE public.salon_id_salon_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.salon_id_salon_seq;
       public          postgres    false    227            D           0    0    salon_id_salon_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.salon_id_salon_seq OWNED BY public.salon.id;
          public          postgres    false    226            �            1259    26301    usuario    TABLE     �   CREATE TABLE public.usuario (
    id integer NOT NULL,
    contrasena character varying(80),
    perfil_usuario character varying(12),
    correo character varying(255)
);
    DROP TABLE public.usuario;
       public         heap    postgres    false            �            1259    26300    usuario_id_usuario_seq    SEQUENCE     �   CREATE SEQUENCE public.usuario_id_usuario_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.usuario_id_usuario_seq;
       public          postgres    false    223            E           0    0    usuario_id_usuario_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.usuario_id_usuario_seq OWNED BY public.usuario.id;
          public          postgres    false    222                       2604    26364 	   alumno id    DEFAULT     m   ALTER TABLE ONLY public.alumno ALTER COLUMN id SET DEFAULT nextval('public.alumno_id_alumno_seq'::regclass);
 8   ALTER TABLE public.alumno ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    231    230    231            x           2604    26265 
   carrera id    DEFAULT     p   ALTER TABLE ONLY public.carrera ALTER COLUMN id SET DEFAULT nextval('public.carrera_id_carrera_seq'::regclass);
 9   ALTER TABLE public.carrera ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    216    216            |           2604    26311    coordinador id    DEFAULT     |   ALTER TABLE ONLY public.coordinador ALTER COLUMN id SET DEFAULT nextval('public.coordinador_id_coordinador_seq'::regclass);
 =   ALTER TABLE public.coordinador ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    224    225    225            ~           2604    26354    grupo id    DEFAULT     j   ALTER TABLE ONLY public.grupo ALTER COLUMN id SET DEFAULT nextval('public.grupo_id_grupo_seq'::regclass);
 7   ALTER TABLE public.grupo ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    229    228            z           2604    26284 
   maestro id    DEFAULT     p   ALTER TABLE ONLY public.maestro ALTER COLUMN id SET DEFAULT nextval('public.maestro_id_maestro_seq'::regclass);
 9   ALTER TABLE public.maestro ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    220    220            y           2604    26272 
   materia id    DEFAULT     p   ALTER TABLE ONLY public.materia ALTER COLUMN id SET DEFAULT nextval('public.materia_id_materia_seq'::regclass);
 9   ALTER TABLE public.materia ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    217    218            }           2604    26318    salon id    DEFAULT     j   ALTER TABLE ONLY public.salon ALTER COLUMN id SET DEFAULT nextval('public.salon_id_salon_seq'::regclass);
 7   ALTER TABLE public.salon ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    227    226    227            {           2604    26304 
   usuario id    DEFAULT     p   ALTER TABLE ONLY public.usuario ALTER COLUMN id SET DEFAULT nextval('public.usuario_id_usuario_seq'::regclass);
 9   ALTER TABLE public.usuario ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    222    223    223            7          0    26361    alumno 
   TABLE DATA           j   COPY public.alumno (id, id_grupo, id_carrera, nombre, direccion, estatus, semestre, telefono) FROM stdin;
    public          postgres    false    231   ;N       (          0    26262    carrera 
   TABLE DATA           5   COPY public.carrera (id, nombre_carrera) FROM stdin;
    public          postgres    false    216   XN       1          0    26308    coordinador 
   TABLE DATA           1   COPY public.coordinador (id, nombre) FROM stdin;
    public          postgres    false    225   uN       4          0    26321    grupo 
   TABLE DATA           E   COPY public.grupo (id_materia, id_maestro, id_salon, id) FROM stdin;
    public          postgres    false    228   �N       ,          0    26281    maestro 
   TABLE DATA           P   COPY public.maestro (id, nombre, direccion, telefono, especialidad) FROM stdin;
    public          postgres    false    220   �N       -          0    26287    maestro_materia 
   TABLE DATA           Q   COPY public.maestro_materia (id_materia, id_maestro, horario_clases) FROM stdin;
    public          postgres    false    221   �N       *          0    26269    materia 
   TABLE DATA           Q   COPY public.materia (id, id_carrera, creditos, nombre_materia, cupo) FROM stdin;
    public          postgres    false    218   �N       3          0    26315    salon 
   TABLE DATA           6   COPY public.salon (id, nombre, capacidad) FROM stdin;
    public          postgres    false    227   O       /          0    26301    usuario 
   TABLE DATA           I   COPY public.usuario (id, contrasena, perfil_usuario, correo) FROM stdin;
    public          postgres    false    223   9O       F           0    0    alumno_id_alumno_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.alumno_id_alumno_seq', 1, false);
          public          postgres    false    230            G           0    0    carrera_id_carrera_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.carrera_id_carrera_seq', 1, false);
          public          postgres    false    215            H           0    0    coordinador_id_coordinador_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.coordinador_id_coordinador_seq', 1, false);
          public          postgres    false    224            I           0    0    grupo_id_grupo_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.grupo_id_grupo_seq', 1, false);
          public          postgres    false    229            J           0    0    maestro_id_maestro_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.maestro_id_maestro_seq', 1, false);
          public          postgres    false    219            K           0    0    materia_id_materia_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.materia_id_materia_seq', 1, false);
          public          postgres    false    217            L           0    0    salon_id_salon_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.salon_id_salon_seq', 1, false);
          public          postgres    false    226            M           0    0    usuario_id_usuario_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.usuario_id_usuario_seq', 1, false);
          public          postgres    false    222            �           2606    26366    alumno alumno_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.alumno
    ADD CONSTRAINT alumno_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.alumno DROP CONSTRAINT alumno_pkey;
       public            postgres    false    231            �           2606    26267    carrera carrera_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.carrera
    ADD CONSTRAINT carrera_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.carrera DROP CONSTRAINT carrera_pkey;
       public            postgres    false    216            �           2606    26313    coordinador coordinador_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.coordinador
    ADD CONSTRAINT coordinador_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.coordinador DROP CONSTRAINT coordinador_pkey;
       public            postgres    false    225            �           2606    26359    grupo grupo_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.grupo
    ADD CONSTRAINT grupo_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.grupo DROP CONSTRAINT grupo_pkey;
       public            postgres    false    228            �           2606    26286    maestro maestro_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.maestro
    ADD CONSTRAINT maestro_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.maestro DROP CONSTRAINT maestro_pkey;
       public            postgres    false    220            �           2606    26274    materia materia_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.materia
    ADD CONSTRAINT materia_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.materia DROP CONSTRAINT materia_pkey;
       public            postgres    false    218            �           2606    26320    salon salon_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.salon
    ADD CONSTRAINT salon_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.salon DROP CONSTRAINT salon_pkey;
       public            postgres    false    227            �           2606    26306    usuario usuario_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_pkey;
       public            postgres    false    223            �           2606    26372    alumno alumno_id_carrera_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.alumno
    ADD CONSTRAINT alumno_id_carrera_fkey FOREIGN KEY (id_carrera) REFERENCES public.carrera(id);
 G   ALTER TABLE ONLY public.alumno DROP CONSTRAINT alumno_id_carrera_fkey;
       public          postgres    false    216    4737    231            �           2606    26367    alumno alumno_id_grupo_fkey    FK CONSTRAINT     {   ALTER TABLE ONLY public.alumno
    ADD CONSTRAINT alumno_id_grupo_fkey FOREIGN KEY (id_grupo) REFERENCES public.grupo(id);
 E   ALTER TABLE ONLY public.alumno DROP CONSTRAINT alumno_id_grupo_fkey;
       public          postgres    false    228    4749    231            �           2606    26329    grupo grupo_id_maestro_fkey    FK CONSTRAINT        ALTER TABLE ONLY public.grupo
    ADD CONSTRAINT grupo_id_maestro_fkey FOREIGN KEY (id_maestro) REFERENCES public.maestro(id);
 E   ALTER TABLE ONLY public.grupo DROP CONSTRAINT grupo_id_maestro_fkey;
       public          postgres    false    228    220    4741            �           2606    26324    grupo grupo_id_materia_fkey    FK CONSTRAINT        ALTER TABLE ONLY public.grupo
    ADD CONSTRAINT grupo_id_materia_fkey FOREIGN KEY (id_materia) REFERENCES public.materia(id);
 E   ALTER TABLE ONLY public.grupo DROP CONSTRAINT grupo_id_materia_fkey;
       public          postgres    false    4739    228    218            �           2606    26334    grupo grupo_id_salon_fkey    FK CONSTRAINT     y   ALTER TABLE ONLY public.grupo
    ADD CONSTRAINT grupo_id_salon_fkey FOREIGN KEY (id_salon) REFERENCES public.salon(id);
 C   ALTER TABLE ONLY public.grupo DROP CONSTRAINT grupo_id_salon_fkey;
       public          postgres    false    227    228    4747            �           2606    26295 /   maestro_materia maestro_materia_id_maestro_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.maestro_materia
    ADD CONSTRAINT maestro_materia_id_maestro_fkey FOREIGN KEY (id_maestro) REFERENCES public.maestro(id);
 Y   ALTER TABLE ONLY public.maestro_materia DROP CONSTRAINT maestro_materia_id_maestro_fkey;
       public          postgres    false    220    221    4741            �           2606    26290 /   maestro_materia maestro_materia_id_materia_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.maestro_materia
    ADD CONSTRAINT maestro_materia_id_materia_fkey FOREIGN KEY (id_materia) REFERENCES public.materia(id);
 Y   ALTER TABLE ONLY public.maestro_materia DROP CONSTRAINT maestro_materia_id_materia_fkey;
       public          postgres    false    218    221    4739            �           2606    26275    materia materia_id_carrera_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.materia
    ADD CONSTRAINT materia_id_carrera_fkey FOREIGN KEY (id_carrera) REFERENCES public.carrera(id);
 I   ALTER TABLE ONLY public.materia DROP CONSTRAINT materia_id_carrera_fkey;
       public          postgres    false    218    4737    216            7      x������ � �      (      x������ � �      1   #   x�3��*M�S���M�K�R.M,J������ xg      4      x������ � �      ,      x������ � �      -      x������ � �      *      x������ � �      3      x������ � �      /   %   x�3�442615�t��/J��KL�/������� oMR     