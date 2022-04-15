test
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

## Documentation SPHINX
1. Create .reStructured Files 
`sphinx-apidoc -f -o .\doc\source\ .\pywordle\`

2. Create html documentation
`.\make.bat html`

## UI-Files
### Convert UI in Python:
Example: `pyside2-uic .\static\main_window.ui > ui_main_window.py`
