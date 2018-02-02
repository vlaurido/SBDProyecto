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
    set stock = IF(NEW.transaccion='SALIDA', stock-NEW.cantidad_producto, stock+NEW.cantidad_producto)
	where codigo = New.cod_producto_id;

-- STORED PROCEDURES

DELIMITER |
CREATE PROCEDURE tres_mas_vendidos(dateStart DATE, dateEnd DATE)
select arreglo.nombre, sum(d.cantidad)
from facturacionapp_arreglo a, facturacionapp_detallefactura d, facturacionapp_factura f
where a.codigo=d.cod_arreglo_id and d.cod_factura_id=f.id and f.fecha>=dateStart and f.fecha<=dateEnd
group by a.nombre
order by sum(d.cantidad) desc
limit 3;
|
DELIMITER ;

DELIMITER |
CREATE PROCEDURE total_ventas(dateStart DATE, dateEnd DATE)
select sum(a.precio_venta*d.cantidad) as venta
from facturacionapp_arreglo a, facturacionapp_detallefactura d, facturacionapp_factura f
where a.codigo=d.cod_arreglo_id and d.cod_factura_id=f.id and f.fecha>=dateStart and f.fecha<=dateEnd
order by venta
|
DELIMITER ;
--DROP PROCEDURE total_ventas
