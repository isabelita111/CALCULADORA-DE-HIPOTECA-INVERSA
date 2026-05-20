create table calculos(
    cedula varchar(10) NOT NULL primary key,
    valor_inmueble numeric NOT NULL,
    tasa_capitalizacion numeric NOT NULL,
    edad integer NOT NULL,
    plazo_simulacion integer NOT NULL,
    porcentaje_LTV numeric NOT NULL,
    monto_mensual_recibido numeric NOT NULL,
    total_recibido_acumulado numeric NOT NULL,
    saldo_proyectado numeric NOT NULL
);


