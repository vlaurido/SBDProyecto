USE quemonadadb;

-- TRIGGERS

Create TRIGGER logDeleteArreglo
BEFORE DELETE ON facturacionapp_arreglo
For each row
	Insert into facturacionapp_logarreglo(id,fecha,cod_arreglo,operacion)
    VALUES(NULL,CURDATE(),codigo,'Borrado');

Create TRIGGER actualizarStock
AFTER INSERT ON facturacionapp_inventario
For each row
	update facturacionapp_toalla
    set stock = IF(NEW.transaccion='SALIDA', stock-NEW.cantidad_toalla, stock+NEW.cantidad_toalla)
	where codigo = New.cod_toalla_id;

-- STORED PROCEDURES

DROP PROCEDURE tres_mas_vendidos

DELIMITER |
CREATE PROCEDURE tres_mas_vendidos(dateStart DATE, dateEnd DATE)
select a.nombre, sum(d.cantidad)
from facturacionapp_arreglo a, facturacionapp_detallefactura d, facturacionapp_factura f
where a.codigo=d.cod_arreglo_id and d.cod_factura_id=f.id and f.fecha>=dateStart and f.fecha<=dateEnd
group by a.nombre
order by sum(d.cantidad) desc
limit 3;
|
DELIMITER ;

DROP PROCEDURE top_toalla

DELIMITER |
CREATE PROCEDURE top_toalla(dateStart DATE, dateEnd DATE)
select t.codigo, sum(i.cantidad_toalla)
from facturacionapp_toalla t, facturacionapp_inventario i
where t.codigo=i.cod_toalla_id and i.fecha>=dateStart and i.fecha<=dateEnd and transaccion='SALIDA'
group by t.codigo
order  by sum(i.cantidad_toalla) desc
limit 5;
|
DELIMITER ;

DROP PROCEDURE total_ventas

DELIMITER |
CREATE PROCEDURE total_ventas(dateStart DATE, dateEnd DATE)
select sum(a.precio_venta*d.cantidad) as venta
from facturacionapp_arreglo a, facturacionapp_detallefactura d, facturacionapp_factura f
where a.codigo=d.cod_arreglo_id and d.cod_factura_id=f.id and f.fecha>=dateStart and f.fecha<=dateEnd
order by venta
|
DELIMITER ;
