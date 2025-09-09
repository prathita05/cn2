import socket
import dns.resolver

def dns_client(domain="www.youtube.com"):
    try:
        # Step 1: Resolve IP Address
        ip = socket.gethostbyname(domain)
        print(f"IP address of {domain}: {ip}")

        results = [f"Domain: {domain}", f"IP: {ip}"]

        # Step 2: A Records
        print("\nA Records:")
        try:
            for rdata in dns.resolver.resolve(domain, "A"):
                print("A:", rdata.to_text())
                results.append(f"A: {rdata.to_text()}")
        except:
            print("No A record found.")

        # Step 3: MX Records
        print("\nMX Records:")
        try:
            for rdata in dns.resolver.resolve(domain, "MX"):
                print("MX:", rdata.to_text())
                results.append(f"MX: {rdata.to_text()}")
        except:
            print("No MX record found.")

        # Step 4: CNAME Records
        print("\nCNAME Records:")
        try:
            for rdata in dns.resolver.resolve(domain, "CNAME"):
                print("CNAME:", rdata.to_text())
                results.append(f"CNAME: {rdata.to_text()}")
        except:
            print("No CNAME record found.")

        # Step 5: Save results
        with open("dns_log.txt", "w") as f:
            f.write("\n".join(results))

        print("\n✅ Results saved to dns_log.txt")

    except Exception as e:
        print("❌ Error:", e)

# Example run
dns_client("www.youtube.com")
