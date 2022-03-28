# pyWordle

## Database
### Alembic
#### Datebase Migration
##### Create New Migration
alembic revision --autogenerate -m "MIGRATION NAME"

##### Update Migration to head
alembic upgrade head

##### Downgrade Migration to specific migration
alembic downgrade MIGRATION_HASH

### Database App-Compatibilites
Please adjust after every version change!

| Database Version  | App Version |
| :---: | :---: |
| v0.X  | v0.X - current version (v0.1.0) |