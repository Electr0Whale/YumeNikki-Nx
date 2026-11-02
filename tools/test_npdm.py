import json, subprocess

base = {
  "name": "Yume Nikki NX",
  "program_id": "0x0100A1B2C3D40000",
  "program_id_range_min": "0x0100A1B2C3D40000",
  "program_id_range_max": "0x0100A1B2C3D40000",
  "main_thread_stack_size": "0x100000",
  "main_thread_priority": 44,
  "default_cpu_id": 0,
  "process_category": 0,
  "system_resource_size": "0x0",
  "version": 0,
  "signature_key_generation": 0,
  "is_retail": True,
  "pool_partition": 0,
  "is_64_bit": True,
  "address_space_type": 1,
  "optimize_memory_allocation": False,
  "disable_device_address_space_merge": False,
  "enable_alias_region_extra_size": False,
  "prevent_code_reads": False,
  "filesystem_access": {
    "permissions": "0xFFFFFFFFFFFFFFFF"
  },
  "service_host": ["*"],
  "service_access": ["*"],
  "kernel_capabilities": [
    {
      "type": "kernel_flags",
      "value": {
        "highest_thread_priority": 59,
        "lowest_thread_priority": 28,
        "highest_cpu_id": 2,
        "lowest_cpu_id": 0
      }
    },
    {
      "type": "application_type",
      "value": 1
    },
    {
      "type": "min_kernel_version",
      "value": "0x30"
    },
    {
      "type": "handle_table_size",
      "value": 512
    },
    {
      "type": "debug_flags",
      "value": {
        "allow_debug": True,
        "force_debug": False,
        "force_debug_prod": False
      }
    }
  ]
}

with open("/home/ubuntu/yn-build/tools/test_npdm.json", "w") as f:
    json.dump(base, f, indent=2)

res = subprocess.run(["/opt/devkitpro/tools/bin/npdmtool", "/home/ubuntu/yn-build/tools/test_npdm.json", "/home/ubuntu/yn-build/tools/test_modern.npdm"], capture_output=True, text=True)
print("Returncode:", res.returncode)
print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)
