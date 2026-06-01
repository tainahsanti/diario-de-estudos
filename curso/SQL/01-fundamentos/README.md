# 01 - Fundamentos SQL

## Conceitos estudados

### Hierarquia do banco

Instância → Database → Tabela → Registro → Campo

### Tipos de dados

| Tipo | Exemplo |
|--------|----------|
| INT | 10 |
| FLOAT | 10.5 |
| TEXT | "João" |
| DATE | 2025-01-01 |
| DATETIME | 2025-01-01 10:00:00 |
| NULL | Valor ausente |

### Chaves

#### Primary Key

Identifica um registro de forma única.

```sql
CREATE TABLE clientes (
    IdCliente INTEGER PRIMARY KEY
);
```

#### Foreign Key

Relaciona tabelas.

```sql
FOREIGN KEY (IdCliente)
REFERENCES clientes(IdCliente)
```

---

## SELECT

```sql
SELECT *
FROM clientes;
```

---

## WHERE

```sql
SELECT *
FROM clientes
WHERE QtdePontos > 100;
```

---

## ORDER BY

```sql
SELECT *
FROM clientes
ORDER BY QtdePontos DESC;
```

---

## LIMIT

```sql
SELECT *
FROM clientes
LIMIT 10;
```

---

## Aprendizados

- `strftime()` foi a parte mais difícil inicialmente.
- Compreendi melhor quando analisei cada função separadamente:
  - `substr()`
  - `datetime()`
  - `strftime()`
