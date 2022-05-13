from typing import Any, Dict

mmcif_col_types: Dict[str, Any] = {
    "B_iso_or_equiv": float,
    "Cartn_x": float,
    "Cartn_y": float,
    "Cartn_z": float,
    "auth_asym_id": str,
    "auth_atom_id": str,
    "auth_comp_id": str,
    "auth_seq_id": int,
    "group_PDB": str,
    "id": int,
    "label_alt_id": int,
    "label_asym_id": str,
    "label_atom_id": str,
    "label_comp_id": str,
    "label_entity_id": int,
    "label_seq_id": int,
    "occupancy": float,
    "pdbx_PDB_ins_code": str,
    "pdbx_PDB_model_num": int,
    "pdbx_formal_charge": int,
    "type_symbol": str,
}

ANISOU_DF_COLUMNS = [
    "id",
    "type_symbol",
    "pdbx_label_atom_id",
    "pdbx_label_alt_id",
    "pdbx_label_comp_id",
    "pdbx_label_asym_id",
    "pdbx_label_seq_id",
    "pdbx_PDB_ins_code",
    "U[1][1]",
    "U[2][2]",
    "U[3][3]",
    "U[1][2]",
    "U[1][3]",
    "U[2][3]",
    "pdbx_auth_seq_id",
    "pdbx_auth_comp_id",
    "pdbx_auth_asym_id",
    "pdbx_auth_atom_id",
]