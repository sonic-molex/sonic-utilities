"""
Module holding correct dictionaries for test YANG models
"""

one_table_container = {
   "has_rpc_or_action": False,
   "rpcs": [],
   "tables":[
      {
         "description":"TABLE_1 description",
         "name":"TABLE_1",
         "actions":[],
         "static-objects":[
            {
            }
         ]
      }
   ]
}

two_table_containers = {
   "has_rpc_or_action": False,
   "rpcs": [],
   "tables":[
      {
         "description":"TABLE_1 description",
         "name":"TABLE_1",
         "actions":[],
         "static-objects":[
            {

            }
         ]
      },
      {
         "description":"TABLE_2 description",
         "name":"TABLE_2",
         "actions":[],
         "static-objects":[
            {

            }
         ]
      }
   ]
}

one_object_container = {
   "has_rpc_or_action": False,
   "rpcs": [],
   "tables":[
      {
         "description":"TABLE_1 description",
         "name":"TABLE_1",
         "actions":[],
         "static-objects":[
            {
                "name":"OBJECT_1",
                "description":"OBJECT_1 description",
                "actions":[],
                "attrs":[
                ]
            }
         ]
      }
   ]
}

two_object_containers = {
   "has_rpc_or_action": False,
   "rpcs": [],
   "tables":[
      {
         "description":"FIRST_TABLE description",
         "name":"TABLE_1",
         "actions":[],
         "static-objects":[
            {
                "name":"OBJECT_1",
                "description":"OBJECT_1 description",
                "actions":[],
                "attrs":[
                ]
            },
            {
                "name":"OBJECT_2",
                "description":"OBJECT_2 description",
                "actions":[],
                "attrs":[
                ]
            }
         ]
      }
   ]
}

one_list = {
   "has_rpc_or_action": False,
   "rpcs": [],
   "tables":[
      {
         "description":"TABLE_1 description",
         "name":"TABLE_1",
         "actions":[],
         "dynamic-objects":[
            {
                "name":"TABLE_1_LIST",
                "description":"TABLE_1_LIST description",
                "actions":[],
                "keys":[
                    {
                        "name": "key_name",
                        "description": "",
                    }
                ],
                "attrs":[
                ]
            }
         ]
      }
   ]
}

two_lists = {
   "has_rpc_or_action": False,
   "rpcs": [],
   "tables":[
      {
         "description":"TABLE_1 description",
         "name":"TABLE_1",
         "actions":[],
         "dynamic-objects":[
            {
                "name":"TABLE_1_LIST_1",
                "description":"TABLE_1_LIST_1 description",
                "actions":[],
                "keys":[
                    {
                        "name": "key_name1",
                        "description": "",
                    }
                ],
                "attrs":[
                ]
            },
            {
                "name":"TABLE_1_LIST_2",
                "description":"TABLE_1_LIST_2 description",
                "actions":[],
                "keys":[
                    {
                        "name": "key_name2",
                        "description": "",
                    }
                ],
                "attrs":[
                ]
            }
         ]
      }
   ]
}

static_object_complex_1 = {
   "has_rpc_or_action": False,
   "rpcs": [],
   "tables":[
      {
         "description":"TABLE_1 description",
         "name":"TABLE_1",
         "actions":[],
         "static-objects":[
            {
                "name":"OBJECT_1",
                "description":"OBJECT_1 description",
                "actions":[],
                "attrs":[
                    {
                        "name":"OBJ_1_LEAF_1",
                        "description": "OBJ_1_LEAF_1 description",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_LEAF_LIST_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": True,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_CHOICE_1_LEAF_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_CHOICE_1_LEAF_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    }
                ]
            }
         ]
      }
   ]
}

static_object_complex_2 = {
   "has_rpc_or_action": False,
   "rpcs": [],
   "tables":[
      {
         "description":"TABLE_1 description",
         "name":"TABLE_1",
         "actions":[],
         "static-objects":[
            {
                "name":"OBJECT_1",
                "description":"OBJECT_1 description",
                "actions":[],
                "attrs":[
                    {
                        "name":"OBJ_1_LEAF_1",
                        "description": "OBJ_1_LEAF_1 description",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_LEAF_2",
                        "description": "OBJ_1_LEAF_2 description",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_LEAF_LIST_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": True,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_LEAF_LIST_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": True,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_CHOICE_1_LEAF_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_CHOICE_1_LEAF_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_CHOICE_2_LEAF_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_CHOICE_2_LEAF_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                ]
            }
         ]
      }
   ]
}

dynamic_object_complex_1 = {
   "has_rpc_or_action": False,
   "rpcs": [],
   "tables":[
      {
         "description":"TABLE_1 description",
         "name":"TABLE_1",
         "actions":[],
         "dynamic-objects":[
            {
                "name":"OBJECT_1_LIST",
                "description":"OBJECT_1_LIST description",
                "actions":[],
                "attrs":[
                    {
                        "name":"OBJ_1_LEAF_1",
                        "description": "OBJ_1_LEAF_1 description",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_LEAF_LIST_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": True,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_CHOICE_1_LEAF_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_CHOICE_1_LEAF_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    }
                ],
                "keys":[
                    {
                        "name": "KEY_LEAF_1",
                        "description": "KEY_LEAF_1 description",
                    }
                ]
            }
         ]
      }
   ]
}

dynamic_object_complex_2 = {
   "has_rpc_or_action": False,
   "rpcs": [],
   "tables":[
      {
         "description":"TABLE_1 description",
         "name":"TABLE_1",
         "actions":[],
         "dynamic-objects":[
            {
                "name":"OBJECT_1_LIST",
                "description":"OBJECT_1_LIST description",
                "actions":[],
                "attrs":[
                    {
                        "name":"OBJ_1_LEAF_1",
                        "description": "OBJ_1_LEAF_1 description",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_LEAF_2",
                        "description": "OBJ_1_LEAF_2 description",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_LEAF_LIST_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": True,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_LEAF_LIST_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": True,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_CHOICE_1_LEAF_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_CHOICE_1_LEAF_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_CHOICE_2_LEAF_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"OBJ_1_CHOICE_2_LEAF_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    }
                ],
                "keys":[
                    {
                        "name": "KEY_LEAF_1",
                        "description": "KEY_LEAF_1 description",
                    },
                    {
                        "name": "KEY_LEAF_2",
                        "description": "KEY_LEAF_2 description",
                    }
                ]
            }
         ]
      }
   ]
}

choice_complex = {
   "has_rpc_or_action": False,
   "rpcs": [],
   "tables":[
      {
         "description":"TABLE_1 description",
         "name":"TABLE_1",
         "actions":[],
         "static-objects":[
            {
                "name":"OBJECT_1",
                "description":"OBJECT_1 description",
                "actions":[],
                "attrs":[
                    {
                        "name":"LEAF_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name": "GR_1_LEAF_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name": "GR_1_LEAF_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name": "LEAF_LIST_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": True,
                        "units": ""
                    },
                    {
                        "name":"LEAF_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"LEAF_3",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name": "GR_5_LEAF_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name": "GR_5_LEAF_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name": "GR_2_LEAF_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name": "GR_2_LEAF_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name": "GR_3_LEAF_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name": "GR_3_LEAF_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name": "LEAF_LIST_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": True,
                        "units": ""
                    },
                    {
                        "name": "LEAF_LIST_3",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": True,
                        "units": ""
                    },
                ]
            }
         ]
      }
   ]
}

grouping_complex = {
   "has_rpc_or_action": False,
   "rpcs": [],
   "tables":[
      {
         "description":"TABLE_1 description",
         "name":"TABLE_1",
         "actions":[],
         "static-objects":[
            {
                "name":"OBJECT_1",
                "description":"OBJECT_1 description",
                "actions":[],
                "attrs":[
                    {
                        "name":"GR_1_LEAF_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"GR_1_LEAF_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                ]
            },
            {
                "name":"OBJECT_2",
                "description":"OBJECT_2 description",
                "actions":[],
                "attrs":[
                    {
                        "name":"GR_5_LEAF_1",
                        "description": "GR_5_LEAF_1 refine description",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"GR_6_LEAF_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name":"GR_6_LEAF_2",
                        "description": "GR_6_LEAF_2 refine description",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name": "GR_4_LEAF_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name": "GR_4_LEAF_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name": "GR_5_LEAF_LIST_1",
                        "description": "GR_5_LEAF_LIST_1 refine description",
                        "is-mandatory": False,
                        "is-leaf-list": True,
                        "units": ""
                    },
                    {
                        "name": "GR_6_CASE_1_LEAF_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name": "GR_6_CASE_1_LEAF_LIST_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": True,
                        "units": ""
                    },
                    {
                        "name": "GR_6_CASE_2_LEAF_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name": "GR_6_CASE_2_LEAF_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": ""
                    },
                    {
                        "name": "GR_6_CASE_2_LEAF_LIST_1",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": True,
                        "units": ""
                    },
                    {
                        "name": "GR_6_CASE_2_LEAF_LIST_2",
                        "description": "",
                        "is-mandatory": False,
                        "is-leaf-list": True,
                        "units": ""
                    },
                ]
            }
         ]
      }
   ]
}

rpc_action_complex = {
   "has_rpc_or_action": True,
   "rpcs": [
      {
         "name": "GET_STATUS",
         "description": "Get device status",
         "input": [
            {
               "name": "DEVICE_ID",
               "description": "Device identifier",
               "is-mandatory": False,
               "is-leaf-list": False,
               "units": ""
            }
         ],
         "output": [
            {
               "name": "STATUS",
               "description": "Device status",
               "is-mandatory": False,
               "is-leaf-list": False,
               "units": ""
            },
            {
               "name": "ERROR_CODES",
               "description": "",
               "is-mandatory": False,
               "is-leaf-list": True,
               "units": ""
            }
         ],
         "has_output": True
      }
   ],
   "tables": [
      {
         "name": "TABLE_1",
         "description": "TABLE_1 description",
         "actions": [],
         "dynamic-objects": [
            {
               "name": "TABLE_1_LIST",
               "description": "TABLE_1_LIST description",
               "attrs": [
                  {
                     "name": "ATTR_1",
                     "description": "ATTR_1 description",
                     "is-mandatory": False,
                     "is-leaf-list": False,
                     "units": ""
                  }
               ],
               "keys": [
                  {
                     "name": "key_name",
                     "description": ""
                  }
               ],
               "actions": [
                  {
                     "name": "RESET",
                     "description": "Reset list entry",
                     "input": [
                        {
                           "name": "RESET_MODE",
                           "description": "",
                           "is-mandatory": False,
                           "is-leaf-list": False,
                           "units": ""
                        }
                     ],
                     "output": [
                        {
                           "name": "RESULT",
                           "description": "",
                           "is-mandatory": False,
                           "is-leaf-list": False,
                           "units": ""
                        }
                     ],
                     "has_input": True,
                     "has_output": True
                  }
               ]
            }
         ]
      },
      {
         "name": "TABLE_2",
         "description": "TABLE_2 description",
         "actions": [],
         "static-objects": [
            {
               "name": "OBJECT_1",
               "description": "OBJECT_1 description",
               "attrs": [
                  {
                     "name": "OBJ_1_LEAF_1",
                     "description": "OBJ_1_LEAF_1 description",
                     "is-mandatory": False,
                     "is-leaf-list": False,
                     "units": ""
                  }
               ],
               "actions": [
                  {
                     "name": "CONFIGURE",
                     "description": "Configure object action",
                     "input": [
                        {
                           "name": "PARAM_1",
                           "description": "Parameter 1",
                           "is-mandatory": False,
                           "is-leaf-list": False,
                           "units": ""
                        },
                        {
                           "name": "PARAM_LIST_1",
                           "description": "",
                           "is-mandatory": False,
                           "is-leaf-list": True,
                           "units": ""
                        }
                     ],
                     "output": [],
                     "has_input": True,
                     "has_output": False
                  }
               ]
            }
         ]
      }
   ]
}

leaf_with_units = {
   "has_rpc_or_action": False,
   "rpcs": [],
   "tables":[
      {
         "description":"TABLE_1 description",
         "name":"TABLE_1",
         "actions":[],
         "static-objects":[
            {
                "name":"OBJECT_1",
                "description":"OBJECT_1 description",
                "actions":[],
                "attrs":[
                    {
                        "name":"OBJ_1_LEAF_1",
                        "description": "OBJ_1_LEAF_1 description",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": "MHz"
                    },
                    {
                        "name":"OBJ_1_LEAF_2",
                        "description": "OBJ_1_LEAF_2 description",
                        "is-mandatory": False,
                        "is-leaf-list": False,
                        "units": "dBm"
                    }
                ]
            }
         ]
      }
   ]
}
