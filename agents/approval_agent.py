def approve_post(post):
    print("\n--- LINKEDIN POST ---\n")
    print(post)
    print("\n-------------------")

    choice = input("Approve post? (yes/no): ").lower()

    if choice == "yes":
        with open("approved_post.txt", "w", encoding="utf-8") as f:
            f.write(post)
        print("✅ Post saved!")
    else:
        print("❌ Post rejected")
