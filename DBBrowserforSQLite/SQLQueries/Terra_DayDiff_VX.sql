select 	(julianday("Datum_1", 'start of day') - julianday('2020-01-01', 'start of day')) AS DAYSVD1_20200101 ,	
	(strftime('%Y', DatumUmrti))-(strftime(Rok_narozeni)) AS AGE_D,
	(julianday("DatumUmrti", 'start of day') - julianday('2020-01-01','start of day')) AS DAYSD_20200101,	
	IIF("OckovaciLatka_1"IS NOT NULL, 1, 0) AS VD1	
from "main"."Czech" WHERE ("OckovaciLatka_1" IS NOT NULL AND "DatumUmrti" IS NOT NULL )
GROUP BY (strftime('%Y', DatumUmrti))-(strftime(Rok_narozeni)),(julianday("DatumUmrti", 'start of day') - julianday('2020-01-01','start of day'));
