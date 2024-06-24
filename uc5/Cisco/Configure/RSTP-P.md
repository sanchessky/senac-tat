RSTP=S

enable
    configure terminal
        spanning-tree (trabalha apenas com vlans)
        spanning-tree vlan 1-60 root primary
        spanning-tree mode rapid-pvst
