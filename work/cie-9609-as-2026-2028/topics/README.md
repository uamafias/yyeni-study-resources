# Topic directories

Directory names stay numeric because contract IDs, objective IDs and every cross-reference in the build are keyed on the topic number. Everything inside them is named for the topic.

| Directory | Topic | Items | Notes file |
|---|---|---:|---|
| `1.1/` | Enterprise | 85 | `1.1-enterprise.md` |
| `1.2/` | Business structure | 89 | `1.2-business-structure.md` |
| `1.3/` | Size of business | 109 | `1.3-size-of-business.md` |
| `1.4/` | Business objectives | 76 | `1.4-business-objectives.md` |
| `1.5/` | Stakeholders in a business | 45 | `1.5-stakeholders-in-a-business.md` |
| `2.1/` | Human resource management (HRM) | 145 | `2.1-human-resource-management-hrm.md` |
| `2.2/` | Motivation | 168 | `2.2-motivation.md` |
| `2.3/` | Management | 49 | `2.3-management.md` |
| `3.1/` | The nature of marketing | 121 | `3.1-the-nature-of-marketing.md` |
| `3.2/` | Market research | 55 | `3.2-market-research.md` |
| `3.3/` | The marketing mix | 130 | `3.3-the-marketing-mix.md` |
| `4.1/` | The nature of operations | 80 | `4.1-the-nature-of-operations.md` |
| `4.2/` | Inventory management | 40 | `4.2-inventory-management.md` |
| `4.3/` | Capacity utilisation and outsourcing | 33 | `4.3-capacity-utilisation-and-outsourcing.md` |
| `5.1/` | Business finance | 55 | `5.1-business-finance.md` |
| `5.2/` | Sources of finance | 79 | `5.2-sources-of-finance.md` |
| `5.3/` | Forecasting and managing cash flows | 43 | `5.3-forecasting-and-managing-cash-flows.md` |
| `5.4/` | Costs | 105 | `5.4-costs.md` |
| `5.5/` | Budgets | 41 | `5.5-budgets.md` |

Regenerate the upload folder at any time:

```bash
python3 standard/v0.2.0-draft/build/publish_subject.py work/cie-9609-as-2026-2028
```
