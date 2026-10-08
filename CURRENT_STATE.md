# Estado canônico atual

> MODE: CURRENT_LIVING_STATE (camadas datadas; o texto de cada revisão fica como registro).
>
> **Camada 2026-10-08 (fechamento da fase de remediação).** Os nove repositórios do stack estão **públicos** desde 2026-10-07 (D-35 do
> predictor-qualification; licença proprietária, código source-available); o fetch do registro resolve **sem token** (`STACK_READ_TOKEN`
> é opcional, o CI usa o token do job como fallback); CI do `main` verde em `7fb3ae5a` (run 37784280880, inclusive o job "Joint lock
> installs CAIN and the three domains together"); instalação limpa reverificada em 2026-10-08 a partir de clones novos sem credencial
> (`packages/research-transport` e `compat/`: fetch + check + `uv lock --check`; `compat/`: `uv sync --locked` e import de cain 0.4.13rc16,
> transporte 0.1.0rc7, core 3.2.1, ops 4.2.2rc1). O parágrafo seguinte (manhã de 2026-10-07) fica como registro: "privados", "CI vermelho" e
> "precisam do segredo" descrevem aquele momento. Estado vivo do CAIN e lista única de pendências do dono:
> `cain/docs/funding/FUNDING_READINESS_SOURCE_OF_TRUTH.md` (§0 e §8).

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

> **Camada 2026-10-07 (noite):** cain `v0.4.13rc16` (`de5db06b`, wheel `d8fca502…`; código igual ao da rc15, lock pelo registro, R01/D-32)
> adotada na lock conjunta `compat/` e publicada como ecosystem `0.2.2`; qualificada pelas integrações crypto (rc16, reemitida rc16e) e stocks (ciclo 6, reemitido ciclo 7)
> do predictor-qualification (attestations QUALIFIED, D-34); a integração do brasileirão continua na rc13 até o runtime do dono.
> O parágrafo seguinte é o estado de 2026-09-30, preservado (em 2026-10-08 esta camada foi movida para fora do meio da frase dele, sem mudar texto).

> **Atualização 2026-09-30.** A combinação corrente do stack, o que foi validado em conjunto e o estado do ciclo de
> qualificação D-27 estão em [ETAPA_B_INTEGRATED_STACK_20260928.md](ETAPA_B_INTEGRATED_STACK_20260928.md) (seção
> "Atualização de 2026-09-30"). Wheels publicadas: core 3.2.1, ops 4.2.2rc1, ecosystem 0.2.1, protocolo 2.0.0rc2,
> transporte 0.1.0rc7, snapshot 1.0.2rc1, bundle 1.0.1rc1, cain 0.4.13rc15, cripto 1.2.0rc4, brasileirão 0.3.0rc5,
> stocks 0.3.0rc3 (`registries/released_architecture.json`; `registries/compatibility_candidate.json` aponta para os
> commits das tags). As três distribuições de domínio instaladas juntas com o resto do stack carregam no registry
> isoladas, com capital `FORBIDDEN` (`scripts/check_real_plugin_integration.py`, `RELEASED_WHEELS=1`, 2026-09-30).
> O texto abaixo (revisão de 13/09/2026) continua válido para contratos, registry e recibos históricos.

**Revisão:** 13/09/2026. A [reconciliação de fidelidade](docs/maintenance/fidelity-20260913.md)
corrige representação, expiração e mensagens de erro, com regressões automatizadas.
A combinação fixada e seus recibos permanecem preservados; fonte corrigida não
significa nova release ou atualização automática de instalações.

## Estado e autoridade por assunto

| Dimensão | Fonte e interpretação |
|---|---|
| Código em `main` | Contratos, registry opcional, ResearchSnapshotV1 e ResearchBundleV1 incorporados. `git ls-remote origin refs/heads/main` informa a ponta publicada; cada SHA tem sua própria CI. |
| Topologia | [architecture_registry.json](registries/architecture_registry.json): sete repositórios, três domínios predictors e dez pacotes independentes. [Charter](ECOSYSTEM_CHARTER.md) define os limites. |
| Releases e artefatos | [released_architecture.json](registries/released_architecture.json): fontes, URLs e hashes das distribuições registradas. Não é inventário da instalação operacional nem consulta permanente de últimas releases. |
| Combinação testada | [compatibility_candidate.json](registries/compatibility_candidate.json), [integração Core](CORE_INTEGRATION_20260913.md) e [recibo](docs/core_integration_20260913/receipt.json). Pins não acompanham `main` automaticamente. |
| Instalação operacional | Autoridade do respectivo projeto; para CAIN, [estado oficial](https://github.com/leonardosovienski/cain/blob/main/ESTADO_DO_PROJETO.md). Os recibos de instalação deste repositório descrevem as revisões e datas que testaram. |
| Ciência e economia | Protocolos e evidências dos domínios, acessíveis nas fichas abaixo. [harness_registry.json](registries/harness_registry.json) preserva atestados datados; não certifica versões posteriores. |
| Operação e capital | Permissões pertencem aos domínios e à decisão humana explícita. Nenhuma autorização resulta desta organização ou de CI verde. |

A integração Ecosystem `3cfb74bef126c421424c08cc774034b42cae5cd4` tem
[CI](https://github.com/leonardosovienski/ecosystem-predictor/actions/runs/34765563374)
e [segurança](https://github.com/leonardosovienski/ecosystem-predictor/actions/runs/34765563366)
aprovadas. Essa evidência continua vinculada àquela revisão. A baseline documental
acima também tem [CI própria](https://github.com/leonardosovienski/ecosystem-predictor/actions/runs/34765919043).

## Projetos e reprodução

[Core](docs/projects/core.md) · [Ops](docs/projects/ops.md) ·
[Cripto](docs/projects/cripto.md) · [Brasileirão](docs/projects/brasileirao.md) ·
[Stocks](docs/projects/stocks.md) · [CAIN](docs/projects/cain.md).

Cada ficha delimita responsabilidades, interfaces e evidência de integração sem
duplicar o manual do projeto. O [runbook](ECOSYSTEM_RUNBOOK.md) contém os comandos
do Ecosystem. Checkout canônico neste PC: `C:/CAIN/contrato`, branch `main`.

## Manutenção e histórico

Antes de atualizar um registro, confronte sua autoridade, revisão e contexto.
Observe drift real, corrija apenas o escopo afetado e preserve pins e evidências
até nova validação explícita. Não retome ações de auditorias antigas por inferência.

As tabelas e ações de 06/09 foram separadas em
[registro histórico](docs/archive/current-state-20260906.md). O
[índice documental](docs/HISTORICAL_DOCUMENT_INDEX.md) classifica registros,
procedimentos e auditorias. O [registro desta organização](docs/maintenance/organization-20260913.md)
contém baseline, classificação de branches, recuperação e validação.
