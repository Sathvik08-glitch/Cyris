from memory import load_memory, save_memory

print("========== MEMORY TEST ==========\n")

memory = load_memory()

backup = memory.copy()

print("Original Memory:")
print(memory)

memory["test"] = "success"

save_memory(memory)

print("\nTemporary Memory:")
print(load_memory())

# Restore
save_memory(backup)

print("\nMemory Restored.")