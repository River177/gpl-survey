# DBLP Reference Audit

Total cited references audited: **173**

Status counts: OK=130, REVIEW=38, NOT_FOUND=4, ERROR=1, NO_TITLE=0

- **OK**: confident DBLP title match, no metadata discrepancy.
- **REVIEW**: matched but year/venue/title needs a look (see Notes).
- **NOT_FOUND**: no confident DBLP match (preprint-only or title drift).
- **ERROR/NO_TITLE**: API error or missing title field.


## REVIEW — needs manual check (38)

| Key | Bib venue | Bib year | DBLP venue | DBLP year | Sim | Notes |
|---|---|---|---|---|---|---|
| `brown2020language` | NeurIPS | 2020 | CoRR | 2025 | 0.75 | year bib=2020 dblp=2025; title sim=0.75 |
| `chen2023exploring` | KDD | 2024 | SIGKDD Explor. | 2023 | 1.00 | year bib=2024 dblp=2023 |
| `defferrard2016convolutional` | NeurIPS | 2016 | NIPS | 2016 | 1.00 | venue bib='NeurIPS' dblp='NIPS' |
| `devlin2019bert` | arXiv preprint | 2019 | NAACL-HLT | 2019 | 1.00 | bib=arXiv but DBLP venue='NAACL-HLT' (consider upgrading) |
| `fang2022geometryenhanced` | Nature | 2022 | Nat. Mach. Intell. | 2022 | 1.00 | venue bib='Nature' dblp='Nat. Mach. Intell.' |
| `fang2022prompt` | arXiv preprint | 2022 | ICLR | 2025 | 0.86 | year bib=2022 dblp=2025; bib=arXiv but DBLP venue='ICLR' (consider upgrading); title sim=0.86 |
| `fatemi2023talk` | arXiv preprint | 2023 | ICLR | 2024 | 1.00 | year bib=2023 dblp=2024; bib=arXiv but DBLP venue='ICLR' (consider upgrading) |
| `fu2025graphprompting` | arXiv preprint | 2025 | KDD | 2025 | 1.00 | bib=arXiv but DBLP venue='KDD' (consider upgrading) |
| `ge2024psp` | ECML PKDD | 2024 | ECML/PKDD | 2024 | 1.00 | venue bib='ECML PKDD' dblp='ECML/PKDD' |
| `gong2024selfpro` | ECML PKDD | 2024 | ECML/PKDD | 2024 | 1.00 | venue bib='ECML PKDD' dblp='ECML/PKDD' |
| `hamilton2017inductive` | NeurIPS | 2017 | NIPS | 2017 | 1.00 | venue bib='NeurIPS' dblp='NIPS' |
| `hu2021lora` | arXiv preprint | 2021 | ICLR | 2022 | 1.00 | year bib=2021 dblp=2022; bib=arXiv but DBLP venue='ICLR' (consider upgrading) |
| `khoshraftar2025graphit` | arXiv preprint | 2025 | WWW | 2025 | 1.00 | bib=arXiv but DBLP venue='WWW' (consider upgrading) |
| `kim2021how` | ICLR | 2021 | CoRR | 2022 | 1.00 | year bib=2021 dblp=2022 |
| `lachi2024graphfm` | TMLR | 2025 | Trans. Mach. Learn. Res. | 2025 | 1.00 | venue bib='TMLR' dblp='Trans. Mach. Learn. Res.' |
| `lee2024supt` | arXiv preprint | 2024 | Inf. Sci. | 2026 | 1.00 | year bib=2024 dblp=2026; bib=arXiv but DBLP venue='Inf. Sci.' (consider upgrading) |
| `li2023survey` | arXiv preprint | 2023 | IJCAI | 2024 | 1.00 | year bib=2023 dblp=2024; bib=arXiv but DBLP venue='IJCAI' (consider upgrading) |
| `li2023what` | KDD | 2023 | KDD | 2023 | 0.92 | title sim=0.92 |
| `liu2023gitmol` | Others | 2024 | CoRR | 2023 | 1.00 | year bib=2024 dblp=2023 |
| `liu2023one` | arXiv preprint | 2023 | ICLR | 2024 | 1.00 | year bib=2023 dblp=2024; bib=arXiv but DBLP venue='ICLR' (consider upgrading) |
| `liu2023pretrain` | ACM Computing Surveys | 2023 | CoRR | 2021 | 1.00 | year bib=2023 dblp=2021 |
| `pan2023unifying` | TKDE | 2024 | CoRR | 2023 | 1.00 | year bib=2024 dblp=2023 |
| `robinson2023leveraging` | arXiv preprint | 2023 | ICLR | 2023 | 1.00 | bib=arXiv but DBLP venue='ICLR' (consider upgrading) |
| `song2024pure` | Others | 2025 | LoG | 2024 | 1.00 | year bib=2025 dblp=2024 |
| `subramonian2021motifdriven` | AAAI | 2021 | IEEE Trans. Knowl. Data Eng. | 2024 | 1.00 | year bib=2021 dblp=2024; venue bib='AAAI' dblp='IEEE Trans. Knowl. Data Eng.' |
| `wang2022common` | TKDE | 2022 | IEEE Trans. Knowl. Data Eng. | 2023 | 1.00 | year bib=2022 dblp=2023; venue bib='TKDE' dblp='IEEE Trans. Knowl. Data Eng.' |
| `wang2023scientific` | Nature | 2023 | Nat. | 2023 | 1.00 | venue bib='Nature' dblp='Nat.' |
| `wang2025clear` | arXiv preprint | 2025 | PAKDD | 2025 | 1.00 | bib=arXiv but DBLP venue='PAKDD' (consider upgrading) |
| `wang2025multidomain` | arXiv preprint | 2025 | ICML | 2025 | 1.00 | bib=arXiv but DBLP venue='ICML' (consider upgrading) |
| `wu2021selfsupervised` | SIGIR | 2021 | Knowl. Based Syst. | 2025 | 0.86 | year bib=2021 dblp=2025; venue bib='SIGIR' dblp='Knowl. Based Syst.'; title sim=0.86 |
| `wu2023personalized` | TKDE | 2024 | IEEE Trans. Knowl. Data Eng. | 2024 | 1.00 | venue bib='TKDE' dblp='IEEE Trans. Knowl. Data Eng.' |
| `xu2018how` | ICLR | 2018 | ICLR | 2019 | 1.00 | year bib=2018 dblp=2019 |
| `you2020graph` | NeurIPS | 2020 | KDD | 2025 | 0.83 | year bib=2020 dblp=2025; venue bib='NeurIPS' dblp='KDD'; title sim=0.83 |
| `yu2023selfsupervised` | TKDE | 2023 | IEEE Trans. Knowl. Data Eng. | 2024 | 1.00 | year bib=2023 dblp=2024; venue bib='TKDE' dblp='IEEE Trans. Knowl. Data Eng.' |
| `zhai2024sgpt` | arXiv preprint | 2024 | CIKM | 2025 | 1.00 | year bib=2024 dblp=2025; bib=arXiv but DBLP venue='CIKM' (consider upgrading) |
| `zhang2018link` | NeurIPS | 2018 | AsiaCCS | 2020 | 0.70 | year bib=2018 dblp=2020; venue bib='NeurIPS' dblp='AsiaCCS'; title sim=0.70 |
| `zhang2023benchmarking` | ACL | 2024 | Trans. Assoc. Comput. Linguistics | 2024 | 1.00 | venue bib='ACL' dblp='Trans. Assoc. Comput. Linguistics' |
| `zhu2021graph` | WWW | 2021 | IEEE Trans. Neural Networks Learn. Syst. | 2024 | 0.75 | year bib=2021 dblp=2024; venue bib='WWW' dblp='IEEE Trans. Neural Networks Learn. Syst.'; title sim=0.75 |

## NOT_FOUND — no DBLP match (4)

| Key | Bib venue | Bib year | DBLP venue | DBLP year | Sim | Notes |
|---|---|---|---|---|---|---|
| `rosenstein2005transfer` | NeurIPS | 2005 |  |  | 0.44 | no confident DBLP title match |
| `velickovic2018graph` | ICLR | 2018 |  |  | 0.33 | no confident DBLP title match |
| `velickovic2019deep` | ICLR | 2019 |  |  | 0.38 | no confident DBLP title match |
| `zhang2023large` | arXiv preprint | 2023 |  |  | 0.45 | no confident DBLP title match |

## ERROR (1)

| Key | Bib venue | Bib year | DBLP venue | DBLP year | Sim | Notes |
|---|---|---|---|---|---|---|
| `sun2021mocl` | KDD | 2021 |  |  |  | HTTP Error 500: Internal Server Error |

## OK (130)

| Key | Bib venue | Bib year | DBLP venue | DBLP year | Sim | Notes |
|---|---|---|---|---|---|---|
| `cao2023when` | KDD | 2023 | CoRR | 2023 | 1.00 |  |
| `chen2023ultradp` | arXiv preprint | 2023 | CoRR | 2023 | 1.00 |  |
| `chen2024prompt` | arXiv preprint | 2024 | CoRR | 2024 | 1.00 |  |
| `chen2025dagprompt` | WWW | 2025 | WWW | 2025 | 1.00 |  |
| `cheng2023wiener` | AAAI | 2023 | AAAI | 2023 | 1.00 |  |
| `dai2021selfexplainable` | CIKM | 2021 | CIKM | 2021 | 1.00 |  |
| `edwards2023synergpt` | arXiv preprint | 2023 | CoRR | 2023 | 1.00 |  |
| `fang2023universal` | NeurIPS | 2023 | NeurIPS | 2023 | 1.00 |  |
| `finn2017modelagnostic` | ICML | 2017 | ICML | 2017 | 1.00 |  |
| `fu2025edge` | ICLR | 2025 | ICLR | 2025 | 1.00 |  |
| `gao2021making` | ACL | 2021 | ACL/IJCNLP | 2021 | 1.00 |  |
| `gao2024protein` | ICLR | 2024 | ICLR | 2024 | 1.00 |  |
| `ge2023enhancing` | arXiv preprint | 2023 | CoRR | 2023 | 1.00 |  |
| `gong2023prompt` | arXiv preprint | 2023 | CoRR | 2023 | 1.00 |  |
| `grover2016node2vec` | KDD | 2016 | KDD | 2016 | 1.00 |  |
| `guo2023datacentric` | KDD | 2023 | KDD | 2023 | 1.00 |  |
| `hao2024motifbased` | WSDM | 2024 | WSDM | 2024 | 1.00 |  |
| `hasanzadeh2019semiimplicit` | NeurIPS | 2019 | NeurIPS | 2019 | 1.00 |  |
| `hassani2020contrastive` | ICML | 2020 | ICML | 2020 | 1.00 |  |
| `haviv2021bertese` | Others | 2021 | EACL | 2021 | 1.00 |  |
| `he2021bernnet` | NeurIPS | 2021 | NeurIPS | 2021 | 1.00 |  |
| `he2024gretriever` | NeurIPS | 2024 | NeurIPS | 2024 | 1.00 |  |
| `he2024unigraph` | KDD | 2025 | KDD | 2025 | 1.00 |  |
| `he2026gp2f` | arXiv preprint | 2026 | CoRR | 2026 | 1.00 |  |
| `hou2022graphmae` | KDD | 2022 | KDD | 2022 | 1.00 |  |
| `hou2023graphmae2` | WWW | 2023 | WWW | 2023 | 1.00 |  |
| `hu2020gptgnn` | KDD | 2020 | KDD | 2020 | 1.00 |  |
| `hu2020strategies` | ICLR | 2020 | ICLR | 2020 | 1.00 |  |
| `hu_prompt-based_2024` | CIKM | 2024 | CIKM | 2024 | 1.00 |  |
| `huang2023prodigy` | NeurIPS | 2023 | NeurIPS | 2023 | 1.00 |  |
| `huang2025oneprompt` | NeurIPS | 2025 | CoRR | 2025 | 1.00 |  |
| `jia_hepa_2025` | AAAI | 2025 | AAAI | 2025 | 1.00 |  |
| `jiang2020how` | Others | 2020 | Trans. Assoc. Comput. Linguistics | 2020 | 1.00 |  |
| `jiang2021contrastive` | CIKM | 2021 | CIKM | 2021 | 1.00 |  |
| `jiang2021pretraining` | KDD | 2021 | KDD | 2021 | 1.00 |  |
| `jiao_hgmp_2025` | IJCAI | 2025 | IJCAI | 2025 | 1.00 |  |
| `jin2021multiscale` | IJCAI | 2021 | IJCAI | 2021 | 1.00 |  |
| `jin2021node` | WSDM | 2021 | WSDM | 2021 | 1.00 |  |
| `jin2023patton` | ACL | 2023 | ACL | 2023 | 1.00 |  |
| `kim2025grapht5` | arXiv preprint | 2025 | CoRR | 2025 | 1.00 |  |
| `lester2021power` | EMNLP | 2021 | EMNLP | 2021 | 1.00 |  |
| `li2021prefixtuning` | ACL | 2021 | ACL/IJCNLP | 2021 | 1.00 |  |
| `li2023graphadapter` | NeurIPS | 2023 | NeurIPS | 2023 | 1.00 |  |
| `li2023promptbased` | arXiv preprint | 2023 | CoRR | 2023 | 1.00 |  |
| `liu2022ptuning` | ACL | 2022 | ACL | 2022 | 1.00 |  |
| `liu2023graph` | arXiv preprint | 2023 | CoRR | 2023 | 1.00 |  |
| `liu2023graphprompt` | WWW | 2023 | WWW | 2023 | 1.00 |  |
| `liu2023molca` | EMNLP | 2023 | EMNLP | 2023 | 1.00 |  |
| `liu2024revisiting` | NeurIPS | 2024 | NeurIPS | 2024 | 1.00 |  |
| `long2022pretraining` | Others | 2022 | Bioinform. | 2022 | 1.00 |  |
| `long2024moat` | CIKM | 2024 | CIKM | 2024 | 1.00 |  |
| `long2024towards` | arXiv preprint | 2024 | CoRR | 2024 | 1.00 |  |
| `lv2025graphprompter` | ICDE | 2025 | ICDE | 2025 | 1.00 |  |
| `ma2023hetgpt` | WWW | 2024 | WWW | 2024 | 1.00 |  |
| `maoliniyazi2026apkgc` | Others | 2026 | Knowl. Based Syst. | 2026 | 1.00 |  |
| `niepert2016learning` | ICML | 2016 | ICML | 2016 | 1.00 |  |
| `ou2016asymmetric` | KDD | 2016 | KDD | 2016 | 1.00 |  |
| `pan2018adversarially` | IJCAI | 2018 | IJCAI | 2018 | 1.00 |  |
| `park2019symmetric` | ICCV | 2019 | ICCV | 2019 | 1.00 |  |
| `park2023graphguided` | arXiv preprint | 2023 | CoRR | 2023 | 1.00 |  |
| `peng2020graph` | WWW | 2020 | WWW | 2020 | 1.00 |  |
| `perozzi2014deepwalk` | KDD | 2014 | KDD | 2014 | 1.00 |  |
| `qian2023can` | arXiv preprint | 2023 | CoRR | 2023 | 1.00 |  |
| `qin2021learning` | NAACL | 2021 | NAACL-HLT | 2021 | 1.00 |  |
| `qiu2020gcc` | KDD | 2020 | KDD | 2020 | 1.00 |  |
| `ren2024surveyllmgraph` | KDD | 2024 | KDD | 2024 | 1.00 |  |
| `rong2020selfsupervised` | NeurIPS | 2020 | NeurIPS | 2020 | 1.00 |  |
| `schick2021fewshot` | EMNLP | 2021 | EMNLP | 2021 | 1.00 |  |
| `schick2021it` | NAACL | 2021 | NAACL-HLT | 2021 | 0.94 |  |
| `shi2021masked` | IJCAI | 2021 | IJCAI | 2021 | 1.00 |  |
| `shi2024graphdomain` | Others | 2025 | J. Comput. Sci. Technol. | 2025 | 1.00 |  |
| `shin2020autoprompt` | EMNLP | 2020 | EMNLP | 2020 | 1.00 |  |
| `shirkavand2023deep` | arXiv preprint | 2023 | CoRR | 2023 | 1.00 |  |
| `sun2020infograph` | ICLR | 2020 | ICLR | 2020 | 1.00 |  |
| `sun2021heterogeneous` | WSDM | 2021 | WSDM | 2021 | 1.00 |  |
| `sun2022gppt` | KDD | 2022 | KDD | 2022 | 1.00 |  |
| `sun2023all` | KDD | 2023 | KDD | 2023 | 1.00 |  |
| `suresh2021adversarial` | NeurIPS | 2021 | NeurIPS | 2021 | 1.00 |  |
| `tan2023s2gae` | WSDM | 2023 | WSDM | 2023 | 1.00 |  |
| `tan2023virtual` | KDD | 2023 | KDD | 2023 | 1.00 |  |
| `thakoor2021bootstrapped` | ICLR | 2021 | CoRR | 2021 | 1.00 |  |
| `tian2023graph` | AAAI | 2024 | AAAI | 2024 | 1.00 |  |
| `tsimpoukelli2021multimodal` | NeurIPS | 2021 | NeurIPS | 2021 | 1.00 |  |
| `wang2017mgae` | CIKM | 2017 | CIKM | 2017 | 1.00 |  |
| `wang2019hyperbolic` | AAAI | 2019 | AAAI | 2019 | 1.00 |  |
| `wang2021selfsupervised` | WWW | 2021 | WWW | 2021 | 1.00 |  |
| `wang2021selfsuperviseda` | KDD | 2021 | KDD | 2021 | 1.00 |  |
| `wang2023chatvideo` | arXiv preprint | 2023 | CoRR | 2023 | 1.00 |  |
| `wang2023knowledge` | AAAI | 2024 | AAAI | 2024 | 1.00 |  |
| `wang2024ddiprompt` | CIKM | 2024 | CIKM | 2024 | 1.00 |  |
| `wang2025does` | ICML | 2025 | ICML | 2025 | 1.00 |  |
| `wang_multihgpt_2025` | Others | 2025 | Inf. Process. Manag. | 2025 | 1.00 |  |
| `wen2023augmenting` | SIGIR | 2023 | SIGIR | 2023 | 1.00 |  |
| `wen2023voucher` | CIKM | 2023 | CIKM | 2023 | 1.00 |  |
| `wu2023promptandalign` | CIKM | 2023 | CIKM | 2023 | 1.00 |  |
| `wu2023survey` | arXiv preprint | 2023 | CoRR | 2023 | 1.00 |  |
| `wu2024graphshifts` | arXiv preprint | 2024 | CoRR | 2024 | 1.00 |  |
| `wu2024promptddg` | ICML | 2024 | ICML | 2024 | 1.00 |  |
| `xie2022selfsupervised` | ICML | 2022 | ICML | 2022 | 1.00 |  |
| `xie2023selfsupervised` | Others | 2023 | IEEE Trans. Pattern Anal. Mach. Intell. | 2023 | 1.00 |  |
| `xu2021infogcl` | NeurIPS | 2021 | NeurIPS | 2021 | 1.00 |  |
| `xu2024graphfm` | arXiv preprint | 2024 | CoRR | 2024 | 1.00 |  |
| `yan2024igap` | WWW | 2024 | WWW | 2024 | 1.00 |  |
| `yang2023datacentric` | Others | 2025 | IEEE Trans. Big Data | 2025 | 1.00 |  |
| `yang2023empirical` | NeurIPS | 2023 | NeurIPS | 2023 | 1.00 |  |
| `yang2024graphpro` | WWW | 2024 | WWW | 2024 | 1.00 |  |
| `yi2023contrastive` | Others | 2024 | ACM Trans. Inf. Syst. | 2024 | 1.00 |  |
| `yu2022are` | SIGIR | 2022 | SIGIR | 2022 | 1.00 |  |
| `yu2025dygprompt` | ICLR | 2025 | ICLR | 2025 | 1.00 |  |
| `yu2025pronog` | KDD | 2025 | KDD | 2025 | 1.00 |  |
| `yu2025samgpt` | WWW | 2025 | WWW | 2025 | 1.00 |  |
| `yu_event-aware_2025` | arXiv preprint |  | CoRR | 2025 | 1.00 |  |
| `yu_hgprompt_2024` | AAAI | 2024 | AAAI | 2024 | 1.00 |  |
| `zhang2019prone` | IJCAI | 2019 | IJCAI | 2019 | 1.00 |  |
| `zhang2020graphbert` | arXiv preprint | 2020 | CoRR | 2020 | 1.00 |  |
| `zhang2023structure` | WWW | 2023 | WWW | 2023 | 1.00 |  |
| `zhang2023videollama` | EMNLP | 2023 | EMNLP | 2023 | 1.00 |  |
| `zhang2024collaborate` | WWW | 2024 | WWW | 2024 | 1.00 |  |
| `zhang2024gpt4rec` | SIGIR | 2024 | SIGIR | 2024 | 1.00 |  |
| `zhao2023gimlet` | NeurIPS | 2023 | NeurIPS | 2023 | 1.00 |  |
| `zhao2023graphglow` | KDD | 2023 | KDD | 2023 | 1.00 |  |
| `zhao2024all` | KDD | 2024 | KDD | 2024 | 1.00 |  |
| `zhao2024hegraphadapter` | arXiv preprint | 2024 | CoRR | 2024 | 1.00 |  |
| `zhao2024p2tag` | KDD | 2024 | KDD | 2024 | 1.00 |  |
| `zhu2023graphcontrol` | WWW | 2024 | WWW | 2024 | 1.00 |  |
| `zhu2023sglpt` | arXiv preprint | 2023 | CoRR | 2023 | 1.00 |  |
| `zhu2024relief` | KDD | 2025 | KDD | 2025 | 1.00 |  |
| `zhu2025llmasgnn` | arXiv preprint | 2025 | CoRR | 2025 | 1.00 |  |
| `zhu2026ffclkgc` | Others | 2026 | Expert Syst. Appl. | 2026 | 1.00 |  |
| `zolnai2024stage` | Others | 2024 | CoRR | 2024 | 1.00 |  |
