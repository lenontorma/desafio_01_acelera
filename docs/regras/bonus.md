# 📖 Cálculo do Bônus Final

Este documento descreve a fórmula e as constantes utilizadas para calcular o bônus final dos funcionários válidos.

---

## Constante Base

Para o cálculo, é utilizada uma constante de valor fixo, definida como `BONUS_BASE`.

* **`BONUS_BASE`** = `1000`

---

## Fórmula de Cálculo

O bônus final de cada funcionário é calculado utilizando a seguinte fórmula:

bonus_final = BONUS_BASE + (salario * bonus_percentual)

Onde:
* `salario` é o valor do salário do funcionário.
* `bonus_percentual` é o valor do bônus percentual (entre 0 e 1).

Este cálculo é aplicado apenas a registros que passaram em todas as regras de validação.
