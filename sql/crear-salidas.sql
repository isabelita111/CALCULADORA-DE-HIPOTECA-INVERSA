create table salidas(
    id_calculo text NOT NULL primary key,
    monto_mensual_recibido numeric NOT NULL,
    total_recibido_acumulado numeric NOT NULL,
    saldo_proyectado numeric NOT NULL
);