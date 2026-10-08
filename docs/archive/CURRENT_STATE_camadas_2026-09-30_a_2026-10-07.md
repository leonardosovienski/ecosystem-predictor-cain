# CURRENT_STATE — camadas de 2026-09-30 e 2026-10-07 movidas do documento vivo

> MODE: SNAPSHOT_IMMUTABLE · AS_OF_DATE: 2026-10-07 · AS_OF_SHA: 6ef10f6 · SUPERSEDED_BY: CURRENT_STATE.md (camada 2026-10-08)
> (registro datado; os parágrafos abaixo foram recortados sem alteração de `CURRENT_STATE.md` em 2026-10-08 para que o documento vivo carregue só o estado atual)

> **Atualização 2026-10-07 (R01, supply chain).** Os repositórios de produto são privados desde o início de 2026-10 e este
> repositório foi renomeado `ecosystem-predictor-cain` em 2026-10-05 (o nome antigo é o showcase público, sem releases);
> toda URL `releases/download/` fixada nos locks respondia 404 e o CI do `main` está vermelho desde 2026-10-04 (último run
> 37627597341). Remediação na branch `claude/cain-audit-remediation-fiwdei`: `packages/research-transport/STACK_WHEELS.json`
> e `compat/STACK_WHEELS.json` registram as wheels (repositório, tag, asset, sha256) e `scripts/stack_wheels.py` as baixa pela
> API para `.stack-wheels/` antes do `uv sync` (ver [runbook](ECOSYSTEM_RUNBOOK.md#wheels-do-stack-registro-canônico));
> `compat/` e os checks de drift precisam do segredo `STACK_READ_TOKEN`. As URLs em `registries/released_architecture.json`
> e `registries/compatibility_candidate.json` são registro histórico das releases, não caminho de instalação.
> Os links de CI abaixo apontam para o nome antigo do repositório e redirecionam enquanto o GitHub mantiver o redirect
> de Actions; o repositório `ecosystem-predictor` atual não é este.

> **Atualização 2026-09-30.** A combinação corrente do stack, o que foi validado em conjunto e o estado do ciclo de
> qualificação D-27 estão em [ETAPA_B_INTEGRATED_STACK_20260928.md](ETAPA_B_INTEGRATED_STACK_20260928.md) (seção
> "Atualização de 2026-09-30"). Wheels publicadas: core 3.2.1, ops 4.2.2rc1, ecosystem 0.2.1, protocolo 2.0.0rc2,
> transporte 0.1.0rc7, snapshot 1.0.2rc1, bundle 1.0.1rc1, cain 0.4.13rc15, cripto 1.2.0rc4, brasileirão 0.3.0rc5,
> stocks 0.3.0rc3 (`registries/released_architecture.json`; `registries/compatibility_candidate.json` aponta para os
> commits das tags). As três distribuições de domínio instaladas juntas com o resto do stack carregam no registry
> isoladas, com capital `FORBIDDEN` (`scripts/check_real_plugin_integration.py`, `RELEASED_WHEELS=1`, 2026-09-30).
> O texto abaixo (revisão de 13/09/2026) continua válido para contratos, registry e recibos históricos.
