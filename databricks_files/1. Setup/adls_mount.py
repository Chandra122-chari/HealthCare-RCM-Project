# Databricks notebook source
storageAccountName = "hrcmproject"
storageAccountAccessKey = dbutils.secrets.get('hrcm-db-kv', 'hrcm-adls-key')
mountPoints=["gold","silver","bronze","landing","configs"]
for mountPoint in mountPoints:
    if not any(mount.mountPoint == f"/mnt/{mountPoint}" for mount in dbutils.fs.mounts()):
        try:
            dbutils.fs.mount(
            source = "wasbs://{}@{}.blob.core.windows.net".format(mountPoint, storageAccountName),
            mount_point = f"/mnt/{mountPoint}",
            extra_configs = {'fs.azure.account.key.' + storageAccountName + '.blob.core.windows.net': storageAccountAccessKey}
            )
            print(f"{mountPoint} mount succeeded!")
        except Exception as e:
            print("mount exception", e)

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

display(dbutils.fs.ls('/mnt/bronze'))
