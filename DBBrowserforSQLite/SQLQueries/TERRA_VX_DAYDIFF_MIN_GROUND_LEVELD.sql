-- this query uses the DB View "VX_DAYDIFF_MIN" which was created using the query "TERRA_VX_DAYDIFF_MIN.SQL"
select AGE_D, DAYSD_20200101, DAYDIFF - MINDAYDIFF AS DAYSD_FORM_VXD1_MIN_GROUND_LEVELD from VX_DAYDIFF_MIN
--select * from VX_DAYDIFF_MIN