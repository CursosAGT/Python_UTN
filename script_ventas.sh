# respaldo ventas de archivos
DATE=$(date --date= +%Y-%m-%d)
HOME="/home/server/Server"
BACKUP="/home/Backup"
#Crear archivo .tar
tar -cf $BACKUP/respaldo_ventas_$DATE.tar $HOME/Ventas/*
#Agregar mas archivos
#tar -rf $BACKUP/respaldo_pendientes_$DATE.tar $HOME/Admin-TNT-MITHRIL/Deudas_y_Gastos_vs_tnt_mithril/
#Comprimir el archivo generado
gzip --best $BACKUP/respaldo_ventas_$DATE.tar
chmod -R 777 /home/Backup/*

